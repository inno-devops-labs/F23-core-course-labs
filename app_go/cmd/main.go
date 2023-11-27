package main

import (
	"app_go/internals/handlers"
	"log"
	"net/http"
	"os"
)

func main() {
	timeHandler := handlers.NewTimeHandler()

	port := os.Getenv("APP_GO_PORT")
	if port == "" {
		port = "8080"
	}
	addr := ":" + port

	http.HandleFunc("/", timeHandler.CurrentTime)

	log.Printf("Server is starting on port %s...", port)

	if err := http.ListenAndServe(addr, nil); err != nil {
		log.Fatalf("Failed to start server: %v", err)
	}

}
