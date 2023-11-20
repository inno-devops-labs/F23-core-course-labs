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
	visitIncrement()
	tpl_index.Execute(w, data)
}

func healthHandler(w http.ResponseWriter, r *http.Request) {
	color.Green("Health check from " + r.RemoteAddr + " OK")
	w.WriteHeader(http.StatusOK)
}

func visitIncrement() VisitData {
	file, err := os.OpenFile("visits", os.O_RDWR|os.O_CREATE, 0666)
	if err != nil {
		color.Red("Could not visit file")
		return VisitData{}
	}
	defer file.Close()

	// Read the visit count from the file
	var visitCount int
	_, err = fmt.Fscan(file, &visitCount)
	if err != nil && err != io.EOF {
		color.Red("Could not read file")
		return VisitData{}
	}

	visitCount++

	// Write the updated visit count back to the file
	_, err = file.Seek(0, 0)
	if err != nil {
		color.Red("Could not seek file")
		return VisitData{}
	}
	_, err = fmt.Fprint(file, visitCount)
	if err != nil {
		color.Red("Could not write to file")
		return VisitData{}
	}
	return VisitData{VisitCount: visitCount}
}

func visitsHandler(w http.ResponseWriter, r *http.Request) {
	visitData := visitIncrement()
	color.Green("Request from " + r.RemoteAddr + " on /visits")
	tpl_visits.Execute(w, visitData)
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
