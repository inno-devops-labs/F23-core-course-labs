package routes

import (
	"goapp/timeutils"
	"io"
	"net/http"
	"time"
	"github.com/prometheus/client_golang/prometheus"
	"github.com/prometheus/client_golang/prometheus/promauto"
	"github.com/prometheus/client_golang/prometheus/promhttp"
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

func handleTime(w http.ResponseWriter, r *http.Request) {
	opsProcessed.Inc()
	start := time.Now()
	_, err := io.WriteString(w, "Hello! Time in Innopolis: "+timeutils.GetTime())
	if err != nil {
		panic("writeString failed")
	}
	execTime.Observe(time.Since(start).Seconds())
}


func SetupRoutes() {
	http.HandleFunc("/time", handleTime)
	http.Handle("/metrics", promhttp.Handler())
}
