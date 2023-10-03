package timeutils

import (
	"time"
)

func GetTime() string {
	loc, err := time.LoadLocation("Europe/Moscow")
	if err != nil {
		panic(err)
	}
	t := time.Now().In(loc).Format("15:04:05")
	return t
}
