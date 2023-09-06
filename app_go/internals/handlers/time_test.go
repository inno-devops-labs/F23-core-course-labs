package handlers

import (
	"io/ioutil"
	"net/http"
	"net/http/httptest"
	"strings"
	"testing"
)

func TestCurrentTime(t *testing.T) {
	timeHandler := NewTimeHandler()

	req := httptest.NewRequest(http.MethodGet, "/", nil)
	rec := httptest.NewRecorder()

	timeHandler.CurrentTime(rec, req)

	res := rec.Result()
	body, _ := ioutil.ReadAll(res.Body)

	if res.StatusCode != http.StatusOK {
		t.Errorf("Unexpected status code: %v", res.StatusCode)
	}

	if !strings.Contains(string(body), "Current Time:") {
		t.Errorf("Unexpected response body: %v", string(body))
	}
}
