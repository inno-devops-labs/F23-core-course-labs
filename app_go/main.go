package main

import (
	"fmt"
	"log"

	"github.com/lcensies/redirector/routes"
	"github.com/lcensies/redirector/utils"
	ginprometheus "github.com/mcuadros/go-gin-prometheus"
)

func main() {

	router := routes.NewRouter()

	prometheusExporter := ginprometheus.NewPrometheus("gin")
	prometheusExporter.Use(router)

	err := router.Run(fmt.Sprintf(":%v", utils.GetEnv("PORT", "8080")))
	if err != nil {
		log.Fatalf("Router error: %v", err)
	}
}
