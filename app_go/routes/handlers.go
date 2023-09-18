package routes

import (
	"app_go/config"
	"app_go/entity"
	"app_go/utils"
	"html/template"
	"net/http"
)

var cfg = config.NewConfig()

func MainHandler(w http.ResponseWriter, r *http.Request) {
	t, err := template.ParseFiles("templates/page.html")
	if err != nil {
		return
	}
	err = t.Execute(w, &entity.Page{Title: "DevOps lab", Msg: "Hello! This is DevOps course lab by Safina Alina", Href: "/joke", LinkMsg: "Read Chuck Norris joke"})
	if err != nil {
		return
	}

}

func JokeHandler(w http.ResponseWriter, r *http.Request) {
	var joke entity.Joke
	if cfg.ServerHost == "0.0.0.0" {
		joke = utils.GetRandomJoke()
	} else {
		err := utils.GetJson("http://api.chucknorris.io/jokes/random", &joke)
		if err != nil {
			return
		}
	}
	t, err := template.ParseFiles("templates/page.html")
	if err != nil {
		return
	}
	err = t.Execute(w, &entity.Page{Title: "DevOps lab", Msg: joke.Value, Href: "/", LinkMsg: "Main page"})
	if err != nil {
		return
	}

}
