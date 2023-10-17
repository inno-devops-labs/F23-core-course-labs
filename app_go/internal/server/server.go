package server

import (
	"app/internal/exchange"
	"fmt"
	"log"
	"net/http"
)

// Available crypto currencies
var cryptoCurrencies = []string{"BTC", "ETH", "DOGE", "SOL"}

type Server struct {
	exchangeRepo exchange.ExchangeRepo
}

// NewServer is a constructor of server
func NewServer(exchangeRepo exchange.ExchangeRepo) *Server {
	return &Server{
		exchangeRepo: exchangeRepo,
	}
}

// Run is a method that start server procedure
func (s *Server) Run(serverPort string) error {
	err := s.serverMux(serverPort)
	return err
}

// server multiplexer
func (s *Server) serverMux(serverPort string) error {
	mux := http.NewServeMux()
	mux.HandleFunc("/", s.requestHandler)
	err := http.ListenAndServe(serverPort, mux)
	return err
}

// handler of requests
func (s *Server) requestHandler(res http.ResponseWriter, req *http.Request) {
	switch req.Method {
	case http.MethodGet:
		log.Println("Get Request from", req.Host)
		s.get(res, req)
	default:
		log.Println("Get Request for unsupported method with key:", req.Method)
		res.Write([]byte(fmt.Sprintf("Unsupported method with key: [%s]\n", req.Method)))
	}
}

// get is a handler of get request for root request
func (s *Server) get(w http.ResponseWriter, req *http.Request) {
	html := "<html><body>"

	// get rates for all available crypto currencies
	for _, cryptoCurrency := range cryptoCurrencies {
		rate, err := s.exchangeRepo.GetExchangeRate(cryptoCurrency, "USD")
		if err != nil {
			html += fmt.Sprintf("<p>Error getting exchange rate for %s: %s</p>", cryptoCurrency, err.Error())
			continue
		}
		html += fmt.Sprintf("<p>1 %s = %.2f USD</p>", cryptoCurrency, rate)
	}

	// write result
	html += "</body></html>"
	w.Header().Set("Content-Type", "text/html")
	w.Write([]byte(html))
}
