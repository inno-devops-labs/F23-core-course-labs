package routes

import (
    "github.com/gin-gonic/gin"
)

func NewRouter() *gin.Engine {
    router := gin.Default()
	router.GET("/", RedirectRequestHandler)
    
    return router
}