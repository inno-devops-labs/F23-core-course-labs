package handlers

import (
	"fmt"
	"log"
	"net/http"
	"time"
)

type TimeHandler struct{}

func NewTimeHandler() *TimeHandler {
	return &TimeHandler{}
}

func (t *TimeHandler) CurrentTime(w http.ResponseWriter, r *http.Request) {
	timeZone := "Europe/Moscow"
	location, err := time.LoadLocation(timeZone)

	if err != nil {
		err_text := fmt.Sprintf("load location: %v", err)
		log.Print(err_text)
		fmt.Fprintf(w, err_text)
	} else {
		currentTime := time.Now().In(location)
		fmt.Fprintf(w, "Current Time: %s", currentTime.Format(time.DateTime))
	}
}
