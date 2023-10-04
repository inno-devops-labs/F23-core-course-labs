package main

import (
	"fmt"
	"log"

	"github.com/lcensies/redirector/routes"
	"github.com/lcensies/redirector/utils"
)

func main() {
	router := routes.NewRouter()
	err := router.Run(fmt.Sprintf(":%v", utils.GetEnv("PORT", "8080")))
	if err != nil {
		log.Fatalf("Router error: %v", err)
	}
}
