package main

import (
	"fmt"
	"html/template"
	"io"
	"net/http"
	"os"
	"time"

	"github.com/fatih/color"
	"github.com/prometheus/client_golang/prometheus/promhttp"
)

type TimeData struct {
	MoscowTime string
}

type VisitData struct {
	VisitCount int
}

var tpl_index = template.Must(template.ParseFiles("templates/index.html"))
var tpl_visits = template.Must(template.ParseFiles("templates/visits.html"))

func indexHandler(w http.ResponseWriter, r *http.Request) {
	loc, _ := time.LoadLocation("Europe/Moscow")
	now := time.Now().In(loc)
	moscowTime := now.Format("02/01/2006 15:04:05")
	data := TimeData{
		MoscowTime: moscowTime,
	}
	color.Green("Request from " + r.RemoteAddr)
	tpl_index.Execute(w, data)
}

func healthHandler(w http.ResponseWriter, r *http.Request) {
	color.Green("Health check from " + r.RemoteAddr + " OK")
	w.WriteHeader(http.StatusOK)
}

func visitsHandler(w http.ResponseWriter, r *http.Request) {
	file, err := os.OpenFile("visits", os.O_RDWR|os.O_CREATE, 0666)
	if err != nil {
		http.Error(w, "Could not open file", http.StatusInternalServerError)
		return
	}
	defer file.Close()

	// Read the visit count from the file
	var visitCount int
	_, err = fmt.Fscan(file, &visitCount)
	if err != nil && err != io.EOF {
		http.Error(w, "Could not read file", http.StatusInternalServerError)
		return
	}

	visitCount++

	// Write the updated visit count back to the file
	_, err = file.Seek(0, 0)
	if err != nil {
		http.Error(w, "Could not seek file", http.StatusInternalServerError)
		return
	}
	_, err = fmt.Fprint(file, visitCount)
	if err != nil {
		http.Error(w, "Could not write file", http.StatusInternalServerError)
		return
	}
	data := VisitData{
		VisitCount: visitCount,
	}
	tpl_visits.Execute(w, data)
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
	mux.Handle("/metrics", promhttp.Handler())
	mux.HandleFunc("/visits", visitsHandler)
	http.ListenAndServe(":"+port, mux)
}
