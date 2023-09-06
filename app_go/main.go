package main

import (
	"github.com/gin-gonic/gin"
	"github.com/lcensies/redirector/controllers"
)

func main() {
	apiRoutes := gin.Default()
	apiRoutes.GET("/", controllers.RedirectRequestHandler)
	apiRoutes.Run()
}
