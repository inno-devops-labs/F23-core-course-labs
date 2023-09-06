package main

import (
	"github.com/lcensies/redirector/routes"
	"github.com/lcensies/redirector/utils"
	"fmt"
)

func main() {
	router := routes.NewRouter()
	router.Run(fmt.Sprintf(":%v", utils.GetEnv("PORT", "8080")))
}
