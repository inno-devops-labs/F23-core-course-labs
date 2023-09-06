package routes

import (
    "github.com/gin-gonic/gin"
    "net/http"
    "net/url"
    "github.com/lcensies/redirector/utils"
)

func RedirectRequestHandler(c *gin.Context) {
    defaultURL := utils.GetEnv("DEFAULT_REDIRECT_URL", "https://www.quora.com")
	location, ok := c.GetQuery("q")
	var link url.URL
	if !ok {
		link = url.URL{Path: defaultURL}
    
	} else {
		link = url.URL{Path: location} 
	}
	c.Redirect(http.StatusFound, link.RequestURI())
}
