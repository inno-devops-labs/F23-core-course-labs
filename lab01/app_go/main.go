package main

import (
	"fmt"
	"log"
	"net/http"
	"time"
)

func main() {
	location, err := time.LoadLocation("Europe/Moscow")
	if err != nil {
		log.Fatal(err)
	}

	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		currentTime := time.Now().In(location)
		fmt.Fprintf(w, currentTime.Format("2006-01-02 15:04:05"))
	})

	if err := http.ListenAndServe(":9000", nil); err != nil {
		log.Fatal(err)
	}
}
