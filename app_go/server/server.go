package server

import (
	"fmt"
	"goapp/routes"
	"log"
	"net/http"
)

func StartServer(port int) {
	log.Printf("Starting server on port %v", port)
	routes.SetupRoutes()
	err := http.ListenAndServe(fmt.Sprintf(":%d", port), nil)
	if err != nil {
		log.Fatal("ListenAndServe: ", err)
	}
}
