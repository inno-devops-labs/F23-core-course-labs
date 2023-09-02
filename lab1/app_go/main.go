package main

import (
	"fmt"
	"goapp/server"
	"os"
	"strconv"
	_ "time/tzdata"
)

func parseArgs() map[string]string {
	args := os.Args
	usage := func(additional_msg string) {
		fmt.Println(additional_msg)
		fmt.Printf("usage: %s <port-number>\n", args[0])
	}
	if len(args) != 2 {
		usage("arguments number mismatch")
	}
	var portStr = args[1]
	_, err := strconv.Atoi(portStr)
	if err != nil {
		usage("expected a port number")
	}
	argMap := map[string]string{"port": portStr}
	return argMap
}

func main() {
	argMap := parseArgs()
	port, _ := strconv.Atoi(argMap["port"])
	server.StartServer(port)
}
