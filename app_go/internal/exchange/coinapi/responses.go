package coinapi

// ExchangeRateResponse is a struct of response from coinapi
type ExchangeRateResponse struct {
	Time         string  `json:"time"`
	AssetIDBase  string  `json:"asset_id_base"`
	AssetIDQoute string  `json:"asset_id_quote"`
	Rate         float64 `json:"rate"`
}
