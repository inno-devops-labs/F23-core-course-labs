package middlewares

import (
	"net/http"

	"github.com/prometheus/client_golang/prometheus"
	"github.com/prometheus/client_golang/prometheus/promauto"
)

var (
	httpRequestsTotal = promauto.NewCounterVec(
		prometheus.CounterOpts{
			Name: "http_requests_total",
			Help: "Numer of HTTP requests",
		},
		[]string{"method", "path"},
	)
)

func PrometheusMetrics(next http.Handler) http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		httpRequestsTotal.With(prometheus.Labels{"method": r.Method, "path": r.URL.Path}).Inc()
		next.ServeHTTP(w, r)
	})
}
