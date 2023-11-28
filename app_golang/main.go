package main

import (
	"fmt"
	"net/http"
	"time"
	"io/ioutil"
	"strconv"
)

func main() {
	fmt.Println("Open on http://localhost:8080/")
	http.HandleFunc("/", timeHandler)
	http.HandleFunc("/visits", visitsHandler)
	http.ListenAndServe(":8080", nil)
}

func timeHandler(w http.ResponseWriter, r *http.Request) {
	// Set the timezone to MSK (Moscow Standard Time)
	location, err := time.LoadLocation("Europe/Moscow")
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

	// Get the current time in the specified timezone
	currentTime := time.Now().In(location)

	// Format the time as a string
	timeStr := currentTime.Format("2006-01-02 15:04:05 MST")

	// Write the time to the HTTP response
	fmt.Fprintf(w, "Current time in MSK timezone: %s\n", timeStr)

	visits, err := ioutil.ReadFile("./volume/visits")
	visitsInt, err := strconv.Atoi(string(visits))
	visitsInt++
	visits = []byte(strconv.Itoa(visitsInt))
	err = ioutil.WriteFile("./volume/visits", visits, 0644)
}

func visitsHandler(w http.ResponseWriter, r *http.Request) {
	// Read the file "./volume/visits"
	visits, err := ioutil.ReadFile("./volume/visits")
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

	// Write the number of visits to the HTTP response
	fmt.Fprintf(w, "Number of visits: %s\n", visits)
}