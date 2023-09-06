package routes

import (
    "net/http"
    "net/http/httptest"
    "testing"
    "github.com/stretchr/testify/assert"
)

func TestPerformsRedirect(t *testing.T) {
    router := NewRouter()
    w := httptest.NewRecorder()
    req, _ := http.NewRequest("GET", "/", nil)
    router.ServeHTTP(w, req)
    assert.Equal(t, 302, w.Code)
}

func TestRedirectsToUrl(t *testing.T) {
    router := NewRouter()
    w := httptest.NewRecorder()
    req, _ := http.NewRequest("GET", "/", nil)
    link := "https://google.com"
    
    q := req.URL.Query()
    q.Add("q", link)
    req.URL.RawQuery = q.Encode()
 
    router.ServeHTTP(w, req)
    assert.Contains(t, w.Body.String(), link)
}
