package routes

import (
	"app_go/config"
	"app_go/entity"
	"app_go/utils"
	"html/template"
	"log"
	"net/http"
)

var cfg = config.NewConfig()

func MainHandler(w http.ResponseWriter, r *http.Request) {
	if r.URL.Path != "/" {
		t, err := template.ParseFiles("templates/not_found.html")
		if err != nil {
			return
		}
		w.WriteHeader(http.StatusNotFound)
		err = t.Execute(w, &entity.Page{})
		if err != nil {
			return
		}
		log.Println(r.Method, r.URL, r.Proto, 404)

	} else {
		t, err := template.ParseFiles("templates/page.html")
		if err != nil {
			return
		}
		w.WriteHeader(http.StatusOK)
		err = t.Execute(w, &entity.Page{Title: "DevOps lab", Msg: "Hello! This is DevOps course lab by Safina Alina", Href: "/joke", LinkMsg: "Read Chuck Norris joke"})
		if err != nil {
			return
		}
		log.Println(r.Method, r.URL, r.Proto, 200)
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
	w.WriteHeader(http.StatusOK)
	err = t.Execute(w, &entity.Page{Title: "DevOps lab", Msg: joke.Value, Href: "/", LinkMsg: "Main page"})
	if err != nil {
		return
	}
	log.Println(r.Method, r.URL, r.Proto, 200)

}
