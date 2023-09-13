package handlers

import (
	"fmt"
	"net/http"
	"time"
)

type TimeHandler struct{}

func NewTimeHandler() *TimeHandler {
	return &TimeHandler{}
}

func (t *TimeHandler) CurrentTime(w http.ResponseWriter, r *http.Request) {
	currentTime := time.Now()
	fmt.Fprintf(w, "Current Time: %s", currentTime)
}
