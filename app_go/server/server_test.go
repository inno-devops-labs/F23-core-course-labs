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
	"time"
)

func randInt(min int, max int) int {
	return min + rand.Intn(max-min)
}

func TestStartServer(t *testing.T) {
	getFreePort := func() int {
		for i := 0; i < 10; i++ {
			port := randInt(1024, 65534)
			dial, err := net.Dial("tcp", "127.0.0.1:"+strconv.Itoa(port))
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
	endpoint_url := "http://127.0.0.1:" + strconv.Itoa(serverPort) + "/time"
	// Wait for the server to start
	MAX_ATTEMPTS := 5
	attempt := 1
	var result *http.Response
	for {
		attempt++
		res, err := http.Get(endpoint_url)
		if err != nil || res.StatusCode > 299 {
			if attempt >= MAX_ATTEMPTS {
				if err != nil {
					t.Fatal("No response from the server: " + endpoint_url)
				} else if res.StatusCode > 299 {
					t.Fatal("HTTP Error: " + strconv.Itoa(res.StatusCode))
				}
			}
			time.Sleep(1 * time.Second)
		} else {
			result = res
			break
		}
	}
	body, err := io.ReadAll(result.Body)
	if err != nil {
		panic(err)
	}
	body_str := string(body)
	if !strings.Contains(body_str, "Time in Innopolis:") {
		t.Fatal("Unexpected /time response, received:" + body_str)
	}
}
