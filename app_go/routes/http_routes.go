package routes

import (
	"goapp/timeutils"
	"io"
	"net/http"
)

func handleTime(w http.ResponseWriter, r *http.Request) {
	_, err := io.WriteString(w, "Hello! Time in Innopolis: "+timeutils.GetTime())
	if err != nil {
		panic("writeString failed")
	}
}

func SetupRoutes() {
	http.HandleFunc("/time", handleTime)
}
