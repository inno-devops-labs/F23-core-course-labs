package routes

import (
	"net/http"
	"net/url"

	"github.com/gin-gonic/gin"
	"github.com/lcensies/redirector/utils"
	"github.com/rs/zerolog/log"
)

// Redirects user to the URL specified by the "q" query
// parameter. Supports fallback to the default URL if no
// parameter was provided.
func RedirectRequestHandler(c *gin.Context) {
	defaultURL := utils.GetEnv("DEFAULT_REDIRECT_URL", "https://www.quora.com")
	location, ok := c.GetQuery("q")
	var link url.URL
	if !ok {
		link = url.URL{Path: defaultURL}

	} else {
		link = url.URL{Path: location}
	}

	err := IncrementVisits(c)
	if err != nil {
		log.Error().Msgf("Failed to increment visits: %v", err)
	}

	c.Redirect(http.StatusFound, link.RequestURI())
}
