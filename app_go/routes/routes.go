package routes

import (
	"github.com/gin-gonic/gin"
)

// Aggregates routes of the application
func NewRouter() *gin.Engine {
	router := gin.Default()
	router.GET("/", RedirectRequestHandler)
	router.GET("/visits", VisitsRequestHandler)

	return router
}
