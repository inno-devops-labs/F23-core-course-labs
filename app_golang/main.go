package main

import (
 "fmt"
 "log"
 "net/http"
 "time"
)

func main() {
 http.HandleFunc("/", handler)
 log.Fatal(http.ListenAndServe(":8008", nil))
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

 return currentTime.Format(time.RFC3339), nil
}