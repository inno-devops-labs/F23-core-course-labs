package routes

import (
	"goapp/timeutils"
	"io"
	"net/http"
	"time"
	"github.com/prometheus/client_golang/prometheus"
	"github.com/prometheus/client_golang/prometheus/promauto"
	"github.com/prometheus/client_golang/prometheus/promhttp"
	"fmt"
	"os"
	"strconv"
	"sync"
)

var (
	opsProcessed = promauto.NewCounter(prometheus.CounterOpts{
			Name: "app_go_processed_ops_total",
			Help: "The total number of processed events",
	})
	execTime = promauto.NewHistogram(prometheus.HistogramOpts{
			Name:    "app_go_execution_time_seconds",
			Help:    "The execution time in seconds",
			Buckets: prometheus.LinearBuckets(0.1, 0.1, 10),
	})
)

type Visits struct {
	visitsFileLock sync.Mutex
	filePath       string
}

func NewVisits(filePath string) *Visits {
	if filePath == "" {
		filePath = "/appdata/visits.txt"
	}
	v := &Visits{
		filePath: filePath,
	}
	v.initVisitsFile()
	return v
}

func (v *Visits) initVisitsFile() int {
	visits := 0

	_, err := os.Stat(v.filePath)
	if os.IsNotExist(err) {
		// If the file doesn't exist, create it and write '0'
		file, err := os.Create(v.filePath)
		if err != nil {
			fmt.Println("Error creating visits file:", err)
			return visits
		}
		defer file.Close()

		file.WriteString(strconv.Itoa(visits))
	} else {
		// If the file exists, read the visits count
		visits, err = v.readVisitsFile()
		if err != nil {
			fmt.Println("Error reading visits file:", err)
			return visits
		}
	}

	return visits
}

func (v *Visits) readVisitsFile() (int, error) {

	file, err := os.Open(v.filePath)
	if err != nil {
		return 0, err
	}
	defer file.Close()

	var visits int
	_, err = fmt.Fscanf(file, "%d", &visits)
	if err != nil {
		return 0, err
	}

	return visits, nil
}

func (v *Visits) writeVisitsFile(newVal int) error {

	file, err := os.Create(v.filePath)
	if err != nil {
		return err
	}
	defer file.Close()

	_, err = fmt.Fprint(file, newVal)
	return err
}

func (v *Visits) IncrementVisits() error {
	v.visitsFileLock.Lock()
	defer v.visitsFileLock.Unlock()

	visits, err := v.readVisitsFile()
	if err != nil {
		return err
	}

	err = v.writeVisitsFile(visits + 1)
	return err
}

func (v *Visits) GetVisits() (int, error) {
	v.visitsFileLock.Lock()
	defer v.visitsFileLock.Unlock()

	return v.readVisitsFile()
}

var visits *Visits;

func handleVisits(w http.ResponseWriter, r *http.Request) {
	visitsCount, err := visits.GetVisits()
	if err != nil {
		panic("getVisits failed")
	}
	// marshal result to json
	_, err = io.WriteString(w, "{\"visits\": "+strconv.Itoa(visitsCount)+"}")
	if err != nil {
		panic("writeString failed")
	}
}

func handleTime(w http.ResponseWriter, r *http.Request) {
	visits.IncrementVisits()
	opsProcessed.Inc()
	start := time.Now()
	_, err := io.WriteString(w, "Hello! Time in Innopolis: "+timeutils.GetTime())
	if err != nil {
		panic("writeString failed")
	}
	execTime.Observe(time.Since(start).Seconds())
}

func SetupRoutes() {
	visits = NewVisits("")
	http.HandleFunc("/time", handleTime)
	http.HandleFunc("/visits", handleVisits)
	http.Handle("/metrics", promhttp.Handler())
}
