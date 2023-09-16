package utils

import (
	"fmt"
	"github.com/joho/godotenv"
	"io/ioutil"
	"net/http"
	"os"
)

func GetWeather(city string) string {
	godotenv.Load(".env")
	token := os.Getenv("KEY")
	fmt.Println(token)
	fmt.Println(city)
	response, err := http.Get(fmt.Sprintf("http://api.weatherapi.com/v1/current.json?key=%s&q=%s\"", token, city))
	if err != nil {
		return "Lol"
	}
	all, err := ioutil.ReadAll(response.Body)
	if err != nil {
		return err.Error()
	}
	return string(all)
}
