package main

import (
	"app/internal/exchange/coinapi"
	. "app/internal/server"
	"log"
)

const (
	serverPort = ":9000"
	apikey     = "DD547DAB-BAEC-477A-A111-F76BC75A2278"
)

func main() {
	// create client for coinapi
	coinapiClient := coinapi.NewClient(apikey)

	// create server and run
	server := NewServer(coinapiClient)
	err := server.Run(serverPort)
	if err != nil {
		log.Fatal(err)
	}
}
