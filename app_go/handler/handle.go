package handler

import (
	"app_go/utils"
	"html/template"
	"log"
	"net/http"
)

func Error(err error) {
	if err != nil {
		log.Println(err.Error())
	}
}

func IndexHandler(w http.ResponseWriter, r *http.Request) {
	html := template.Must(template.ParseFiles("templates/index.html"))
	city := r.URL.Path[1:]
	result := utils.Parse(city)
	if result.Err == nil {
		err := html.Execute(w, city+" temperature is "+result.Celsius)
		Error(err)
		return
	}
	err := html.Execute(w, result.Err.Error())
	Error(err)
}
