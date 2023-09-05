package routes

import (
	"app_go/entity"
	"app_go/utils"

	"html/template"
	"net/http"
)

func MainHandler(w http.ResponseWriter, r *http.Request) {
	t, err := template.ParseFiles("templates/page.html")
	if err != nil {
		return
	}
	err = t.Execute(w, &entity.Page{Title: "Lab 1", Msg: "Hello! This is DevOps course lab 1 by Safina Alina", Href: "/joke", LinkMsg: "Read Chuck Norris joke"})
	if err != nil {
		return
	}

}

func JokeHandler(w http.ResponseWriter, r *http.Request) {
	var joke entity.Joke
	err := utils.GetJson("https://api.chucknorris.io/jokes/random", &joke)
	if err != nil {
		return
	}
	t, err := template.ParseFiles("templates/page.html")
	if err != nil {
		return
	}
	err = t.Execute(w, &entity.Page{Title: "Lab 1", Msg: joke.Value, Href: "/", LinkMsg: "Main page"})
	if err != nil {
		return
	}

}
