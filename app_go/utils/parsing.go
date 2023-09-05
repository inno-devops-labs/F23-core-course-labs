package utils

import (
	"app_go/entities"
	"github.com/gocolly/colly"
)

func Parse(city string) entities.Weather {
	c := colly.NewCollector()
	var result entities.Weather
	c.OnHTML("div.today-temperature span[dir=ltr]", func(element *colly.HTMLElement) {
		result.Celsius = element.Text
	})
	err := c.Visit("https://www.meteoprog.com/weather/" + city + "/")
	if err != nil {
		result.Err = err
		return result
	}
	result.Err = nil
	return result
}
