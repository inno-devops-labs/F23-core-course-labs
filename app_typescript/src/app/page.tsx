"use client";

import { useEffect, useState } from "react";
import styles from "./page.module.css";

export default function Home() {
  const [currencies, setCurrencies] = useState<[string, number][]>([]);

  useEffect(() => {
    fetch(
      "https://v6.exchangerate-api.com/v6/3a3668edc99c8b365ba538a1/latest/USD"
    ).then(async (data) => {
      const currencyData = JSON.parse(await data.text());
      const entries = Object.entries(currencyData.conversion_rates) as [
        string,
        number
      ][];
      entries.sort((a, b) => a[1] - b[1]);

      setCurrencies(entries);
    });
  }, []);

  console.log(currencies);

  return (
    <main className={styles.main}>
      <h1>USD exchange rate</h1>
      {currencies.map((currency) => (
        <p key={currency[0]}>
          {currency[0]}: {currency[1]}
        </p>
      ))}
    </main>
  );
}
