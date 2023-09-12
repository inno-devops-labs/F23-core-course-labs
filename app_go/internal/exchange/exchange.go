package exchange

// ExchangeRepo is a interface for getting the exchange rate
type ExchangeRepo interface {
	GetExchangeRate(baseCurrency string, quoteCurrnecy string) (float64, error)
}
