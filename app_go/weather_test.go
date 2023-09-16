package main

import (
	"app_go/handler"
	"app_go/utils"
	"fmt"
	"github.com/stretchr/testify/assert"
	"net/http"
	"net/http/httptest"
	"strings"
	"testing"
)

func getData(s string) string {
	data := strings.Split(s, "<p>")
	res := strings.Split(data[1], "</p>")
	return res[0]
}

func TestExistCities(t *testing.T) {
	cities := []string{
		"kazan", "moscow", "innopolis", "astana", "almaty",
	}

	for _, city := range cities {
		request, _ := http.NewRequest(http.MethodGet, "/"+city, nil)
		response := httptest.NewRecorder()

		handler.IndexHandler(response, request)

		assert.Equal(t, response.Code, 200)

		result := getData(response.Body.String())
		data := strings.Split(result, " ")
		celsius := data[3][5:]

		assert.Equal(t, data[0], city)
		assert.Equal(t, utils.Parse(data[0]).Celsius[1:], celsius)
	}
}

func TestNotExistCities(t *testing.T) {
	tests := []string{
		"lol", "test",
	}

	for _, city := range tests {
		request, _ := http.NewRequest(http.MethodGet, "/"+city, nil)
		response := httptest.NewRecorder()

		handler.IndexHandler(response, request)
		fmt.Println(response.Body.String())
		assert.Equal(t, response.Code, 404)
	}
}
