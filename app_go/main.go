package main

import (
	"fmt"
	"goapp/server"
	"log"
	"os"
	"strconv"
	_ "time/tzdata"
)

func parseArgs() map[string]string {
	args := os.Args
	usage := func(additional_msg string) {
		fmt.Println(additional_msg)
		log.Fatalf("usage: %s <port-number>\n", args[0])
	}
	var portStr = "80" // option 0: use default port
	if len(args) > 2 {
		usage("arguments number mismatch")
	} else if len(args) == 2 { // option 1: get port from command line
		portStr = args[1]
		_, err := strconv.Atoi(portStr)
		if err != nil {
			usage("expected a port number")
		}
	} else { // option 2: get port from environment variable
		if os.Getenv("GOAPP_PORT") != "" {
			portStr = os.Getenv("GOAPP_PORT")
		}
	}
	argMap := map[string]string{"port": portStr}
	return argMap
}

func main() {
	argMap := parseArgs()
	port, _ := strconv.Atoi(argMap["port"])
	server.StartServer(port)
}
