package middleware

import (
	"fmt"
	"log"
	"net/http"
	"os"
	"path/filepath"
	"strconv"
	"time"
)

func addVisit() {
	// Define the directory and file path relative to the current file
	dirPath := "./data"
	filename := filepath.Join(dirPath, "visits.txt")

	// Create the directory if it does not exist
	err := os.MkdirAll(dirPath, 0755)
	if err != nil {
		fmt.Println(err)
		return
	}

	// Check if the file exists
	if _, err := os.Stat(filename); os.IsNotExist(err) {
		// If the file does not exist, create it and write 0 to it
		err := os.WriteFile(filename, []byte("0"), 0644)
		if err != nil {
			fmt.Println("Error creating file:", err)
			return
		}
	}

	// Read the number from the file
	data, err := os.ReadFile(filename)
	if err != nil {
		fmt.Println("Error reading file:", err)
		return
	}

	// Convert the data to a number
	number, err := strconv.Atoi(string(data))
	if err != nil {
		fmt.Println("Error converting to number:", err)
		return
	}

	// Increment the number
	number++

	// Write the new number back to the file
	err = os.WriteFile(filename, []byte(strconv.Itoa(number)), 0644)
	if err != nil {
		fmt.Println("Error writing file:", err)
		return
	}
}

// Logging is middleware for wrapping any handler we want to track response
// times for and to see what resources are requested.
// a visits counting logic
func Logging(next http.Handler) http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		addVisit()
		start := time.Now()
		req := fmt.Sprintf("%s %s", r.Method, r.URL)
		log.Println(req)
		next.ServeHTTP(w, r)
		log.Println(req, "completed in", time.Now().Sub(start))
	})
}
