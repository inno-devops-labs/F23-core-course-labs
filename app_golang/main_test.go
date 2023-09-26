package main

import (
 "net/http"
 "net/http/httptest"
 "testing"
 "strings"
 "time"
)

func TestHandler(t *testing.T) {
	req, err := http.NewRequest("GET", "/", nil)
	if err != nil {
		t.Fatal(err)
	}

	rr := httptest.NewRecorder()
	handler := http.HandlerFunc(handler)

	handler.ServeHTTP(rr, req)

	if status := rr.Code; status != http.StatusOK {
		t.Errorf("handler returned wrong status code: got %v want %v", status, http.StatusOK)
	}

	expectedBodySubstring := "Current time in Moscow:"
	if !strings.Contains(rr.Body.String(), expectedBodySubstring) {
		t.Errorf("handler returned unexpected body: got %v want body substring %v",
			rr.Body.String(), expectedBodySubstring)
	}
}

func TestIndexHandler_ResponseBody(t *testing.T) {
	req, err := http.NewRequest("GET", "/", nil)
	if err != nil {
		t.Fatal(err)
	}

	rr := httptest.NewRecorder()
	handler := http.HandlerFunc(handler)

	handler.ServeHTTP(rr, req)

	now := time.Now().Round(0)
    expectedBodySubstring := string(now.Format("2006-01-02T15:04"))
	
	if !strings.Contains(rr.Body.String(), expectedBodySubstring) {
		t.Errorf("handler returned unexpected body: got %v want body substring %v",
			rr.Body.String(), expectedBodySubstring)
	}
}