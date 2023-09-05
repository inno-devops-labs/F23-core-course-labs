package config

import (
	"log"
	"os"

	"github.com/joho/godotenv"
)

type ServerCfg struct {
	ServerHost string
	ServerPort string
}

func NewConfig() *ServerCfg {
	err := godotenv.Load()
	if err != nil {
		log.Println("Error loading .env file")
	}
	host := os.Getenv("SERVER_HOST")
	if host == "" {
		host = "127.0.0.1"
	}
	port := os.Getenv("SERVER_PORT")
	if port == "" {
		port = "3000"
	}

	return &ServerCfg{ServerHost: host, ServerPort: port}
}
