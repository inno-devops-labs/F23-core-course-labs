package main

import (
	"html/template"
	"net/http"
	"os"
	"time"
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

	tpl.Execute(w, data)
}

func main() {
	port := os.Getenv("PORT")
	if port == "" {
		port = "3000"
	}

	mux := http.NewServeMux()

	mux.HandleFunc("/", indexHandler)
	http.ListenAndServe(":"+port, mux)
}
