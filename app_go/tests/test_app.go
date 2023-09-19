"""
This module contains unit tests for the Go web application.
"""

package main

import (
	"net/http"
	"net/http/httptest"
	"testing"
	"time"
)

func TestMainHandler(t *testing.T) {
	// Create a request to the root URL ("/")
	req, err := http.NewRequest("GET", "/", nil)
	if err != nil {
		t.Fatal(err)
	}

	// Create a response recorder to record the response
	rr := httptest.NewRecorder()

	// Call the main handler function
	mainHandler(rr, req)

	// Check the response status code (should be 200 OK)
	if rr.Code != http.StatusOK {
		t.Errorf("Expected status code %d, got %d", http.StatusOK, rr.Code)
	}

	// Parse the response body and check if it contains the current time in the correct format
	currentTime := time.Now().In(time.FixedZone("Europe/Moscow", 3*60*60)).Format("2006-01-02 15:04:05")
	expectedBody := "Current Moscow Time: " + currentTime
	if rr.Body.String() != expectedBody {
		t.Errorf("Expected response body '%s', got '%s'", expectedBody, rr.Body.String())
	}
}

func TestServer(t *testing.T) {
	// Start a test HTTP server
	ts := httptest.NewServer(http.HandlerFunc(mainHandler))
	defer ts.Close()

	// Send a GET request to the test server
	resp, err := http.Get(ts.URL)
	if err != nil {
		t.Fatal(err)
	}
	defer resp.Body.Close()

	// Check the response status code (should be 200 OK)
	if resp.StatusCode != http.StatusOK {
		t.Errorf("Expected status code %d, got %d", http.StatusOK, resp.StatusCode)
	}

	// Parse the response body and check if it contains the current time in the correct format
	currentTime := time.Now().In(time.FixedZone("Europe/Moscow", 3*60*60)).Format("2006-01-02 15:04:05")
	expectedBody := "Current Moscow Time: " + currentTime
	buf := make([]byte, len(expectedBody))
	_, err = resp.Body.Read(buf)
	if err != nil {
		t.Fatal(err)
	}
	actualBody := string(buf)
	if actualBody != expectedBody {
		t.Errorf("Expected response body '%s', got '%s'", expectedBody, actualBody)
	}
}

func TestMain(t *testing.T) {
	// In the main function, we start an HTTP server, so we can't directly test it here.
	// This test is mainly to check if the main function doesn't cause any panics or errors.
	go main()
	// Give the server some time to start
	time.Sleep(100 * time.Millisecond)
}
