package main

import (
 "net/http"
 "net/http/httptest"
 "testing"
 "strings"
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

	now, err :=  http.NewRequest("GET", "/", nil)

	if err != nil {
		t.Fatal(err)
	}
	
	rn := httptest.NewRecorder()
	handler = http.HandlerFunc(handler)

	handler.ServeHTTP(rn, now)

	left := rr.Body.String()
	right := rn.Body.String()

	if !strings.Contains(left[:len(left)-9], right[:len(right)-9]) {
		t.Errorf("handler returned unexpected body: got %v want body substring %v",
			rr.Body.String(), rn.Body.String())
	}
}