package main

import (
	"fmt"
	"net/http"
	"sync"
	"time"
	"io/ioutil"
	"strconv"
)

var (
	counterMu sync.Mutex
	visits    int
)

func main() {
    // Load initial visit count from the file
	loadVisits()

	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		// Increment visit count for each request
		incrementVisits()

	    // Got current time in Moscow
		loc, _ := time.LoadLocation("Europe/Moscow")
		currentTime := time.Now().In(loc).Format("2006-01-02 15:04:05")

		// Send time in response
		fmt.Fprintf(w, "Current Moscow Time: %s", currentTime)
	})

	http.HandleFunc("/visits", func(w http.ResponseWriter, r *http.Request) {
		// Display recorded visits
		fmt.Fprintf(w, "Total visits: %d\n", getVisits())
	})

	// Listen port 8080
	http.ListenAndServe(":8080", nil)
}

func incrementVisits() {
	counterMu.Lock()
	defer counterMu.Unlock()
	visits++
	saveVisits()
}

func getVisits() int {
	counterMu.Lock()
	defer counterMu.Unlock()
	return visits
}

func saveVisits() {
	counterMu.Lock()
	defer counterMu.Unlock()

	// Save the visits count to a file named 'visits.txt'
	err := ioutil.WriteFile("visits.txt", []byte(strconv.Itoa(visits)), 0644)
	if err != nil {
		fmt.Println("Error saving visits count:", err)
	}
}

func loadVisits() {
	counterMu.Lock()
	defer counterMu.Unlock()

	// Read visits count from 'visits.txt' file if exists
	data, err := ioutil.ReadFile("visits.txt")
	if err == nil {
		count, err := strconv.Atoi(string(data))
		if err == nil {
			visits = count
			return
		}
	}
	// If file doesn't exist or error reading, set visits count to zero
	visits = 0
}
