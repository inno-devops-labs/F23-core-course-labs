package main

import (
	"context"
	"log"
	"net/http"
	"os"
	"os/signal"
	"syscall"

	"github.com/YeslieSnayder/devops-course-labs/app_golang/controller"
	"github.com/YeslieSnayder/devops-course-labs/app_golang/version"
)

// How to try it: PORT=8000 go run main.go
func main() {
	log.Printf(
		"Starting the service...\ncommit: %s, build time: %s, release: %s",
		version.Commit, version.BuildTime, version.Release,
	)

	port := os.Getenv("PORT")
	if port == "" {
		log.Fatal("Port is not set.")
	}

	router := controller.Router(version.BuildTime, version.Commit, version.Release)

	interrupt := make(chan os.Signal, 1)
	signal.Notify(interrupt, os.Interrupt, syscall.SIGTERM)

	srv := http.Server{
		Addr:    ":" + port,
		Handler: router,
	}
	go func() {
		log.Fatal(srv.ListenAndServe())
	}()
	log.Print("The service is ready to listen and serve")

	killSignal := <-interrupt
	switch killSignal {
	case os.Interrupt:
		log.Print("Got SIGINT...")
	case syscall.SIGTERM:
		log.Print("Got SIGTERM...")
	}

	log.Print("Server is shutting down...")
	err := srv.Shutdown(context.Background())
	if err != nil {
		log.Fatal(err)
	}
	log.Print("Done!")
}
