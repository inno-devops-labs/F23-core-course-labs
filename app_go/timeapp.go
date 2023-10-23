package main

import (
	"html/template"
	"net/http"
	"os"
	"time"

	"github.com/fatih/color"
)

type TimeData struct {
	MoscowTime string
}

var tpl = template.Must(template.ParseFiles("templates/index.html"))

func indexHandler(w http.ResponseWriter, r *http.Request) {
	loc, _ := time.LoadLocation("Europe/Moscow")
	now := time.Now().In(loc)
	moscowTime := now.Format("02/01/2006 15:04:05")
	data := TimeData{
		MoscowTime: moscowTime,
	}
	color.Green("Request from " + r.RemoteAddr)
	tpl.Execute(w, data)
}

func healthHandler(w http.ResponseWriter, r *http.Request) {
	color.Green("Health check from " + r.RemoteAddr + " OK")
	w.WriteHeader(http.StatusOK)
}

func main() {
	port := os.Getenv("APP_PORT")
	if port == "" {
		port = "3000"
	}
	mux := http.NewServeMux()
	color.Cyan("Listening on port " + port)
	mux.HandleFunc("/", indexHandler)
	mux.HandleFunc("/health", healthHandler)
	http.ListenAndServe(":"+port, mux)
}
