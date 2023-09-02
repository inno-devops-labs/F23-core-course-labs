package main

import (
	"fmt"
	"github.com/gocolly/colly"
	"net/http"
)

type weather struct {
	c string
}

var result weather

func indexHandler(w http.ResponseWriter, r *http.Request) {
	w.Write([]byte("Innopolis weather is " + result.c + "C"))
}

func main() {
	c := colly.NewCollector()
	c.OnHTML("div.today-temperature span[dir=ltr]", func(e *colly.HTMLElement) {
		result.c = e.Text
		fmt.Println(e.Text)
	})
	c.Visit("https://www.meteoprog.com/weather/Innopolis/")
	mx := http.NewServeMux()
	mx.HandleFunc("/", indexHandler)
	http.ListenAndServe(":3000", mx)
}
