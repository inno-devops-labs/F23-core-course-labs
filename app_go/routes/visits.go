package routes

import (
	"bufio"
	"net/http"
	"os"
	"strconv"

	"github.com/gin-gonic/gin"
	"github.com/lcensies/redirector/utils"
)

var visits int = 0

func IncrementVisits(c *gin.Context) error {

	visitsPath := utils.GetEnv("VISITS_PATH", "/app/data/visits.txt")
	f, err := os.OpenFile(visitsPath, os.O_RDWR|os.O_CREATE, 0600)
	if err != nil {

		return err
	}
	defer f.Close()

	if visits == 0 {
		scanner := bufio.NewScanner(f)
		scanner.Scan()

		visits, err = strconv.Atoi(scanner.Text())
		if err != nil {
			visits = 0
		}
	}

	visits += 1

	f.Truncate(0)
	f.Seek(0, 0)
	f.WriteString(strconv.Itoa(visits))

	return nil
}

// Shows the number of times the application
// has been visited
func VisitsRequestHandler(c *gin.Context) {
	c.Data(http.StatusOK, "text/html; charset=UTF-8", []byte(strconv.Itoa(visits)))
}
