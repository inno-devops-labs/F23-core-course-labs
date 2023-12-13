// Package main starts the simple server and serves HTML
package main

import (
	"app_go/config"
	"app_go/middleware"
	"app_go/routes"
	"fmt"
	"log"
	"net/http"
	"time"
)

func main() {
	cfg := config.NewConfig()
	mux := http.NewServeMux()

	mux.Handle("/time", middleware.Logging(routes.MoscowTime()))

	addr := fmt.Sprintf("%s:%s", cfg.ServerHost, cfg.ServerPort)

	server := http.Server{
		Addr:         addr,
		Handler:      mux,
		ReadTimeout:  15 * time.Second,
		WriteTimeout: 15 * time.Second,
		IdleTimeout:  15 * time.Second,
	}

	log.Println("main: running simple server on", cfg.ServerHost, cfg.ServerPort)
	if err := server.ListenAndServe(); err != nil {
		log.Fatalf("main: couldn't start simple server: %v\n", err)
	}

	err := http.ListenAndServe(cfg.ServerHost+":"+cfg.ServerPort, mux)
	if err != nil {
		return
	}
}
