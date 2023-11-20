package main

import (
	"net/http"
	"net/http/httptest"
	"regexp"
	"strings"
	"testing"
	"time"
)

func TestIndexHandler_StatusOK(t *testing.T) {
	req, err := http.NewRequest("GET", "/", nil)
	if err != nil {
		t.Fatal(err)
	}

	rr := httptest.NewRecorder()
	handler := http.HandlerFunc(indexHandler)

	handler.ServeHTTP(rr, req)

	if status := rr.Code; status != http.StatusOK {
		t.Errorf("handler returned wrong status code: got %v want %v",
			status, http.StatusOK)
	}
}

func TestIndexHandler_ResponseBody(t *testing.T) {
	req, err := http.NewRequest("GET", "/", nil)
	if err != nil {
		t.Fatal(err)
	}

	rr := httptest.NewRecorder()
	handler := http.HandlerFunc(indexHandler)

	handler.ServeHTTP(rr, req)

	expectedBodySubstring := "Moscow"
	if !strings.Contains(rr.Body.String(), expectedBodySubstring) {
		t.Errorf("handler returned unexpected body: got %v want body substring %v",
			rr.Body.String(), expectedBodySubstring)
	}
}

func TestIndexHandler_TimePrecision(t *testing.T) {
	req, err := http.NewRequest("GET", "/", nil)
	if err != nil {
		t.Fatal(err)
	}

	rr := httptest.NewRecorder()
	handler := http.HandlerFunc(indexHandler)

	handler.ServeHTTP(rr, req)

	layout := "02/01/2006 15:04:05"
	re := regexp.MustCompile(`\d{2}/\d{2}/\d{4} \d{2}:\d{2}:\d{2}`)
	match := re.FindString(rr.Body.String())
	loc, _ := time.LoadLocation("Europe/Moscow")
	parsedTime, err := time.ParseInLocation(layout, match, loc)
	currentTime := time.Now().In(loc)
	if err != nil {
		t.Fatal(err)
	}

	diff := parsedTime.Sub(currentTime)
	if diff > time.Second || diff < -time.Second {
		t.Errorf("handler returned imprecise time: got %v, current time is %v",
			parsedTime, currentTime)
	}
}
