package routes

import (
	"fmt"
	"net/http"
	"os"
	"path/filepath"
	"strconv"
)

func getVisits() int {
	// Define the directory and file path relative to the current file
	dirPath := "./data"
	filename := filepath.Join(dirPath, "visits.txt")

	// Read the number from the file
	data, err := os.ReadFile(filename)
	if err != nil {
		fmt.Println("Error reading file:", err)
		return 0
	}

	// Convert the data to a number
	number, err := strconv.Atoi(string(data))
	if err != nil {
		fmt.Println("Error converting to number:", err)
		return 0
	}

	return number
}

func GetVisits() http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		w.Header().Set("Content-Type", "application/json")
		w.WriteHeader(http.StatusOK)
		jsonData := []byte(fmt.Sprintf("{\"visits\":%d}", getVisits()))
		_, err := w.Write(jsonData)
		if err != nil {
			return
		}
	})
}
