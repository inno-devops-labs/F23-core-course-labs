package main

import (
	"fmt"
	"github.com/gocolly/colly"
	"net/http"
)

type weather struct {
	c   string
	err error
}

// var html = template.Must(template.ParseFiles("index.html"))
var result weather

func indexHandler(w http.ResponseWriter, r *http.Request) {
	city := r.URL.Path[1:]
	parse(city)
	if result.err == nil {
		w.Write([]byte("Hello " + city + " " + result.c))
		return
	}
	w.Write([]byte("This city doesn't exist"))
}

func parse(city string) {
	c := colly.NewCollector()
	c.OnHTML("div.today-temperature span[dir=ltr]", func(e *colly.HTMLElement) {
		result.c = e.Text
		fmt.Println(e.Text)
	})
	err := c.Visit("https://www.meteoprog.com/weather/" + city + "/")
	if err != nil {
		result.err = err
		return
	}
	result.err = nil
}

func main() {
	mx := http.NewServeMux()
	mx.HandleFunc("/", indexHandler)
	err := http.ListenAndServe(":3000", mx)
	if err != nil {
		fmt.Println(err.Error())
		return
	}
}
