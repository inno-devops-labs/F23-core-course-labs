import { useState, useEffect } from "react";

import logo from "./logo.svg";
import "./App.css";

const parseDate = (time) => {
  const options = {
    weekday: "short",
    month: "long",
    day: "numeric",
    year: "numeric",
    timeZone: "Europe/Moscow",
  };
  return time.toLocaleDateString("en-US", options);
};

const parseTime = (time) => {
  const options = {
    hour12: false,
    hour: "2-digit",
    minute: "2-digit",
    second: "2-digit",
    timeZone: "Europe/Moscow",
  };
  return time.toLocaleDateString("en-US", options);
};

const App = () => {
  const [time, setTime] = useState(new Date());
  useEffect(() => {
    const interval = setInterval(() => {
      setTime(new Date());
    }, 1000);
    return () => clearInterval(interval);
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <h1>What time is in Moscow now???</h1>
        <p className="App-Date">{parseDate(time)}</p>
        <time data-testid="time-element" className="App-Time">
          {parseTime(time)}
        </time>
        <img src={logo} className="App-logo" alt="logo" />
      </header>
    </div>
  );
};

export default App;
