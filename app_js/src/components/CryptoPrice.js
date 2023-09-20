import React from 'react';

function CryptoPrice({ label, price }) {
  return <p>{label}: ${price}</p>;
}

export default CryptoPrice;
