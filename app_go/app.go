package main

import (
	"fmt"
	"net/http"
	"time"
)

func main() {
	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		// Got current time в Moscow
		loc, _ := time.LoadLocation("Europe/Moscow")
		currentTime := time.Now().In(loc).Format("2006-01-02 15:04:05")

		// Отправляем время в ответе
		fmt.Fprintf(w, "Current Moscow Time: %s", currentTime)
	})

	// Слушаем порт 8080
	http.ListenAndServe(":8080", nil)
}
