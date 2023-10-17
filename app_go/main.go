package main

import (
	"fmt"
	"log"
	"net/http"
	"time"
)

const timeFormat = "2006-01-02 15:04:05"

func currentMoscowTimeHandler(w http.ResponseWriter, r *http.Request) {
	log.Println("GET / HTTP")
	location, err := time.LoadLocation("Europe/Moscow")
	if err != nil {
		log.Println(err)
		http.Error(w, "Internal server error", http.StatusInternalServerError)
	}

	currentTime := time.Now().In(location)
	fmt.Fprint(w, currentTime.Format(timeFormat))
}

func main() {
	http.HandleFunc("/", currentMoscowTimeHandler)
	if err := http.ListenAndServe(":9000", nil); err != nil {
		log.Fatal(err)
	}
}
