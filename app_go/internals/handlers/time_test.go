package handlers

import (
	"io/ioutil"
	"net/http"
	"net/http/httptest"
	"regexp"
	"strings"
	"testing"
	"time"
)

func TestCurrentTime(t *testing.T) {
	timeZone := "Europe/Moscow"
	location, err := time.LoadLocation(timeZone)

	if err != nil {
		t.Errorf("Coudn't load location for: %v", timeZone)
	}
	timeHandler := NewTimeHandler()

	clientTime := time.Now().UTC()
	t.Logf("client time: %v", clientTime.Format(time.DateTime))

	req := httptest.NewRequest(http.MethodGet, "/", nil)
	rec := httptest.NewRecorder()

	timeHandler.ServeHTTP(rec, req)

	res := rec.Result()
	body, _ := ioutil.ReadAll(res.Body)

	content := string(body)

	if res.StatusCode != http.StatusOK {
		t.Errorf("Unexpected status code: %v", res.StatusCode)
	}

	if !strings.Contains(content, "Current Time:") {
		t.Errorf("Unexpected response body: %v", content)
	}

	re := regexp.MustCompile(`\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}`)

	if !re.MatchString(content) {
		t.Errorf("Invalid Response body: %v", content)
	}

	matched := re.FindString(content)

	t.Logf("regex matched: %v", matched)

	serverTime, err := time.ParseInLocation(time.DateTime, matched, location)
	if err != nil {
		t.Errorf("Couldn't not parse: %v", err)
	}
	serverTime = serverTime.UTC()
	t.Logf("server time: %v", serverTime.Format(time.DateTime))

	diff := serverTime.Sub(clientTime).Abs()
	t.Logf("absolute difference between server time and client time: %s", diff)

	maxMargin := 5

	if diff.Seconds() > float64(maxMargin) {
		t.Errorf("The difference between times is more than %v seconds", maxMargin)
	}
}
