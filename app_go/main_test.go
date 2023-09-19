package main

import (
    "net/http"
    "net/http/httptest"
    "testing"
)

func Test_indexHandler(t *testing.T) {
    req, err := http.NewRequest("GET", "http://example.com/foo", nil)
    if err != nil {
        t.Fatal(err)
    }

    res := httptest.NewRecorder()
    indexHandler(res, req)

    exp := "<h1>Hello World!</h1>"
    act := res.Body.String()
    if exp != act {
        t.Fatalf("Expected %s gog %s", exp, act)
    }
}