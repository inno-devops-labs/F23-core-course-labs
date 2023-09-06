package main

import (
	"github.com/lcensies/redirector/routes"
	"github.com/lcensies/redirector/utils"
)

func main() {
	router := routes.NewRouter()
	router.Run(utils.GetEnv("HOST", ":9888"))
}
