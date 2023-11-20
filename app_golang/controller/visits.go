package controller

import (
	"errors"
	"fmt"
	"log"
	"net/http"
	"os"
	"strconv"
	"strings"
	"sync"

	"github.com/gorilla/mux"
)

var (
	dataDirPath    = "data"
	visitsFilePath = dataDirPath + "/visits"
)

func init() {
	path, err := os.Getwd()
	if err != nil {
		log.Printf("ERROR: can't get current working directory: %v", err)

		return
	}

	dataDirPath = path + "/" + dataDirPath
	visitsFilePath = path + "/" + visitsFilePath
	log.Printf("Visits file path: %s", visitsFilePath)

	createVisitsFileIfNotExist()
}

func visits(w http.ResponseWriter, _ *http.Request) {
	createVisitsFileIfNotExist()

	data, err := os.ReadFile(visitsFilePath)
	if err != nil {
		log.Printf("ERROR: can't read file to read visits counter: %v", err)

		w.WriteHeader(http.StatusInternalServerError)

		return
	}

	w.WriteHeader(http.StatusOK)

	if len(data) == 0 {
		_, err = w.Write([]byte("0"))
		if err != nil {
			log.Printf("ERROR: can't write data to response: %v", err)

			w.WriteHeader(http.StatusInternalServerError)
		}

		return
	}

	_, err = w.Write(data)
	if err != nil {
		log.Printf("ERROR: can't write data to response: %v", err)

		w.WriteHeader(http.StatusInternalServerError)
	}
}

func addVisitsCounter(m *sync.Mutex) mux.MiddlewareFunc {
	return func(h http.Handler) http.Handler {
		return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
			defer h.ServeHTTP(w, r)

			m.Lock()
			defer m.Unlock()

			createVisitsFileIfNotExist()

			data, err := os.ReadFile(visitsFilePath)
			if err != nil {
				log.Printf("ERROR: can't read file to read visits counter: %v", err)

				return
			}

			var (
				isEmpty bool
				i       int
			)

			if len(data) == 0 {
				log.Printf("WARNING: visits file is empty")
				isEmpty = true
			}

			if !isEmpty {
				i, err = strconv.Atoi(strings.TrimSpace(string(data)))
				if err != nil {
					log.Printf("ERROR: incorrect data in visits file: %v", err)

					return
				}
			}

			i++
			f, err := os.Create(visitsFilePath)
			if err != nil {
				log.Printf("ERROR: can't create visits file: %v", err)

				return
			}
			defer f.Close()

			_, err = f.WriteString(fmt.Sprintf("%d", i))
			if err != nil {
				fmt.Printf("ERROR: writing new value to visits file: %v", err)
			}
		})
	}
}

func createVisitsFileIfNotExist() {
	if _, err := os.Stat(visitsFilePath); errors.Is(err, os.ErrNotExist) {
		err = os.MkdirAll(dataDirPath, 0777)
		if err != nil {
			log.Printf("ERROR: can't create data directory: %v", err)
		}

		err = os.WriteFile(visitsFilePath, []byte("0"), 0777)
		if err != nil {
			log.Printf("ERROR: can't write to visits file: %v", err)
		}
	}
}
