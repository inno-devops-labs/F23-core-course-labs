import React, { useState, useEffect } from 'react';
import axios from 'axios';
import log from './logger';
import CryptoPrice from './components/CryptoPrice';
import RefreshButton from './components/RefreshButton';

function App() {
  const [cryptoPrices, setCryptoPrices] = useState({ btc: null, eth: null });

    // Define a function to fetch cryptocurrency prices from CoinGecko API
    const fetchData = async () => {
    try {
      // Make API request to get cryptocurrency prices
      const response = await axios.get('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd');
      const { bitcoin, ethereum } = response.data;
      setCryptoPrices({ btc: bitcoin.usd, eth: ethereum.usd });
      log(`Updated the crypto prices! BTC: ${bitcoin.usd}, ETH: ${ethereum.usd}`, 'info');
    } catch (error) {
      log("There was an error fetching the crypto prices!", 'error');
    }
  };
    
  // Use the useEffect hook to fetch prices when the component mounts
  useEffect(() => {
    fetchData();
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <h1>Cryptocurrency Prices</h1>
        <h2>According to Coingecko API</h2>
        <CryptoPrice label="Bitcoin (BTC)" price={cryptoPrices.btc} />
        <CryptoPrice label="Ethereum (ETH)" price={cryptoPrices.eth} />
        <RefreshButton />
      </header>
    </div>
  );
}

export default App;
