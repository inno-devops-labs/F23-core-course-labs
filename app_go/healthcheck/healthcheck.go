package main;

import (
	"os"
	"fmt"
	"net/http"
)

func main() {
	var port string;
	if len(os.Args) < 2 {
		port = "80"
	} else {
		port = os.Args[1]
	}
	_, err := http.Get(fmt.Sprintf("http://localhost:%s/time", port))
	if err != nil {
		os.Exit(1);
	}
}