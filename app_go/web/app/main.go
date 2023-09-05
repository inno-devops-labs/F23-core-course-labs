// Package main starts the simple server and serves HTML
package main

import (
	"fmt"
	"log"
	"net/http"
	"time"
)

// logging is middleware for wrapping any handler we want to track response
// times for and to see what resources are requested.
func logging(next http.Handler) http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		start := time.Now()
		req := fmt.Sprintf("%s %s", r.Method, r.URL)
		log.Println(req)
		next.ServeHTTP(w, r)
		log.Println(req, "completed in", time.Now().Sub(start))
	})
}

func moscowTime() http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		currentTime := time.Now().Format("2006-01-02 15:04:05")

		htmlResponse := `
		<html>
		<body>
			<h1>Current Moscow Time</h1>
			<p>%s</p>
		</body>
		</html>
		`
		_, err := fmt.Fprintf(w, htmlResponse, currentTime)
		if err != nil {
			return
		}
	})
}

func main() {
	mux := http.NewServeMux()
	mux.Handle("/time/", logging(moscowTime()))

	var addr = "127.0.0.1:8070"

	server := http.Server{
		Addr:         addr,
		Handler:      mux,
		ReadTimeout:  15 * time.Second,
		WriteTimeout: 15 * time.Second,
		IdleTimeout:  15 * time.Second,
	}
	log.Println("main: running simple server on port", 8070)
	if err := server.ListenAndServe(); err != nil {
		log.Fatalf("main: couldn't start simple server: %v\n", err)
	}
}
