package main

import (
	"html/template"
	"log"
	"net/http"

	"github.com/gocolly/colly"
)

type weather struct {
	Celsius string
	err     error
}

var result weather

func handleError(err error) {
	if err != nil {
		log.Println(err.Error())
	}
}

func indexHandler(w http.ResponseWriter, r *http.Request) {
	html := template.Must(template.ParseFiles("templates/index.html"))
	city := r.URL.Path[1:]
	parse(city)
	if result.err == nil {
		err := html.Execute(w, city+" temperature is "+result.Celsius)
		handleError(err)
		return
	}
	err := html.Execute(w, result.err.Error())
	handleError(err)
}

func parse(city string) {
	c := colly.NewCollector()
	c.OnHTML("div.today-temperature span[dir=ltr]", func(element *colly.HTMLElement) {
		result.Celsius = element.Text
	})
	err := c.Visit("https://www.meteoprog.com/weather/" + city + "/")
	if err != nil {
		result.err = err
		return
	}
	result.err = nil
}

func main() {
	http.HandleFunc("/", indexHandler)
	err := http.ListenAndServe(":3000", nil)
	handleError(err)
}
