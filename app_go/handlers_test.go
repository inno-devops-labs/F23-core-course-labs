package main

import (
	"app_go/routes"
	"net/http/httptest"
	"strings"
	"testing"
)

func Test_MainHandler(t *testing.T) {
	rr := httptest.NewRecorder()
	req := httptest.NewRequest("GET", "/", nil)
	routes.MainHandler(rr, req)
	if !strings.Contains(rr.Body.String(), "<h1>Hello! This is DevOps course lab") || rr.Code != 200 {
		t.Error("wrong response")
	}
}

func Test_JokeHandler(t *testing.T) {
	rr := httptest.NewRecorder()
	req := httptest.NewRequest("GET", "/joke", nil)
	routes.JokeHandler(rr, req)
	if !strings.Contains(rr.Body.String(), "<h3>&#x2022; <a href=/>Main page</a> </h3>") || rr.Code != 200 {
		t.Error("wrong response")
	}
}
