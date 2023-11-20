package main

import (
 "fmt"
 "net/http"
 "time"
 "os"

 "github.com/fatih/color"
 "github.com/prometheus/client_golang/prometheus"
 "github.com/prometheus/client_golang/prometheus/promhttp"
 dto "github.com/prometheus/client_model/go"
)

var (
 httpRequestsTotal = prometheus.NewCounterVec(
  prometheus.CounterOpts{
   Name: "http_requests_total",
   Help: "Total number of HTTP requests.",
  },
  []string{"method", "status_code"},
 )
)

func init() {
 // Register the metrics with the custom metrics registry
 prometheus.MustRegister(httpRequestsTotal)
}

func main() {
 color.Yellow("Before server started")
 http.HandleFunc("/", handler)
 http.HandleFunc("/healthcheck", healthHandler)
 http.HandleFunc("/visits", visitsHandle)

 // Expose metrics at "/metrics"
 http.Handle("/metrics", promhttp.Handler())

 color.Yellow("Server started")
 http.ListenAndServe(":8008", nil)
}

func handler(w http.ResponseWriter, r *http.Request) {
 // Increment HTTP requests counter
 httpRequestsTotal.With(prometheus.Labels{
  "method":      r.Method,
  "status_code": fmt.Sprintf("%d", http.StatusOK),
 }).Inc()

 // Write to file
 f, err := os.OpenFile("volume/visits", os.O_TRUNC|os.O_CREATE|os.O_WRONLY, 0644)
 if err != nil {
    http.Error(w, err.Error(), http.StatusInternalServerError)
 }
 defer f.Close()
 var m = &dto.Metric{}
 if err := httpRequestsTotal.WithLabelValues("GET", "200").Write(m); err != nil {
     fmt.Fprintf(w, "Error")
 }
 if _, err := f.WriteString(fmt.Sprintf("%f\n", m.Counter.GetValue())); err != nil {
    http.Error(w, err.Error(), http.StatusInternalServerError)
  }

 moscowTime, err := getMoscowTime()
 if err != nil {
  http.Error(w, fmt.Sprintf("Error: %v", err), http.StatusInternalServerError)
  return
 }

 fmt.Fprintf(w, "Current time in Moscow: %s", moscowTime)
}

func healthHandler(w http.ResponseWriter, r *http.Request) {
 fmt.Fprintf(w, "OK")
}

func visitsHandle(w http.ResponseWriter, r *http.Request) {
    var m = &dto.Metric{}
    if err := httpRequestsTotal.WithLabelValues("GET", "200").Write(m); err != nil {
        fmt.Fprintf(w, "Error")
    }
    fmt.Fprintf(w, fmt.Sprintf("%f", m.Counter.GetValue()))
 }
 

func getMoscowTime() (string, error) {
 moscow, err := time.LoadLocation("Europe/Moscow")
 if err != nil {
  return "", err
 }

 currentTime := time.Now().In(moscow)

 color.Yellow("Current Moscow time: " + currentTime.Format(time.RFC3339) + "\n")
 return currentTime.Format(time.RFC3339), nil
}