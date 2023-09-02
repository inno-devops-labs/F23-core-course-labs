package server

import (
	"io"
	"log"
	"math/rand"
	"net"
	"net/http"
	"strconv"
	"strings"
	"testing"
)

func randInt(min int, max int) int {
	return min + rand.Intn(max-min)
}

func TestStartServer(t *testing.T) {
	getFreePort := func() int {
		for i := 0; i < 10; i++ {
			port := randInt(1024, 65534)
			dial, err := net.Dial("tcp", "localhost:"+strconv.Itoa(port))
			if err != nil {
				return port
			} else {
				defer dial.Close()
			}
		}
		log.Fatal("out of attempts for free ports")
		return -1
	}
	serverPort := getFreePort()
	go StartServer(serverPort)
	res, err := http.Get("http://localhost:" + strconv.Itoa(serverPort) + "/time")
	if err != nil {
		t.Fatal("No response from the server")
	} else if res.StatusCode > 299 {
		t.Fatal("HTTP Error: " + strconv.Itoa(res.StatusCode))
	}
	body, err := io.ReadAll(res.Body)
	if err != nil {
		panic(err)
	}
	body_str := string(body)
	if !strings.Contains(body_str, "Time is:") {
		t.Fatal("Unexpected /time response")
	}
}
