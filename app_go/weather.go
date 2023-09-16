package main

import (
	"app_go/utils"
	"fmt"
)

func main() {
	fmt.Println(utils.GetWeather("Kazan"))
	//http.HandleFunc("/", handler.IndexHandler)
	//err := http.ListenAndServe(":3000", nil)
	//handler.Error(err)
}
