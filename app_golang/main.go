package main

import (
    "fmt"
	"github.com/fatih/color"
    "net/http"
    "time"
)


func main() {
    color.Yellow("Before server started")
    http.HandleFunc("/", handler)
    color.Yellow("Server started")
    http.ListenAndServe(":8008", nil)
}

func handler(w http.ResponseWriter, r *http.Request) {
    moscowTime, err := getMoscowTime()
    if err != nil {
        http.Error(w, fmt.Sprintf("Error: %v", err), http.StatusInternalServerError)
    return
    }

    fmt.Fprintf(w, "Current time in Moscow: %s", moscowTime)
}

func getMoscowTime() (string, error) {
    moscow, err := time.LoadLocation("Europe/Moscow")
    if err != nil {
        return "", err
    }

    currentTime := time.Now().In(moscow)

    color.Yellow("Current Moscow time: " + currentTime.Format(time.RFC3339) + "\n")
    return currentTime.Format(time.RFC3339), nil
}