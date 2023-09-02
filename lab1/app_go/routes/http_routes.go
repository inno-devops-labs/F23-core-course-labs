package routes

import (
	"goapp/timeutils"
	"io"
	"net/http"
)

func handleTime(w http.ResponseWriter, r *http.Request) {
	io.WriteString(w, "Hello! Time in Innopolis: "+timeutils.GetTime())
}

func SetupRoutes() {
	http.HandleFunc("/time", handleTime)
}
