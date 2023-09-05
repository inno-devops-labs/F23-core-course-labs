package coinapi

import (
	"app/internal/exchange"
	"encoding/json"
	"errors"
	"fmt"
	"io"
	"net/http"
)

// api url
var URL = "https://rest.coinapi.io"

// check if the client satisfies the interface
var _ exchange.ExchangeRepo = (*Client)(nil)

// Client is a struct of client for coinapi with apikey based on http.Client
type Client struct {
	apiKey string
	http.Client
}

// NewClient is a constructor of Client
func NewClient(apikey string) *Client {
	return &Client{
		apiKey: apikey,
	}
}

// GetExchangeRate is a method that sends a request to coinapi to get the exchange rate
func (cl *Client) GetExchangeRate(baseCurrency string, quoteCurrnecy string) (float64, error) {
	// make url
	url := fmt.Sprint(URL, "/v1/apikey-", cl.apiKey, "/exchangerate/", baseCurrency, "/", quoteCurrnecy)

	// create request
	req, err := http.NewRequest("GET", url, nil)
	if err != nil {
		return 0, err
	}

	// get response
	response, err := cl.Do(req)
	if err != nil {
		return 0, err
	}
	defer response.Body.Close()

	// check status
	if response.StatusCode != http.StatusOK {
		return 0, errors.New("status code not 200")
	}

	// read response
	body, err := io.ReadAll(response.Body)
	if err != nil {
		return 0, err
	}
	var exchangeRateResponse ExchangeRateResponse
	err = json.Unmarshal(body, &exchangeRateResponse)
	if err != nil {
		return 0, nil
	}

	return exchangeRateResponse.Rate, nil
}
