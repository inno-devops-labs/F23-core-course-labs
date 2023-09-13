import { render, screen } from "@testing-library/react";
import App from "./App";

test("renders without errors", () => {
  render(<App />);
});

test("time updates on page refresh", () => {
  render(<App />);

  const currentTime = screen.getByTestId("time-element").textContent;

  setTimeout(() => {
    const updatedTime = screen.getByTestId("time-element").textContent;

    expect(updatedTime).not.toBe(currentTime);
  }, 2000);
});

test("displays the correct date", () => {
  render(<App />);

  const currentDate = new Date().toLocaleDateString("en-US", {
    weekday: "short",
    month: "long",
    day: "numeric",
    year: "numeric",
    timeZone: "Europe/Moscow",
  });

  expect(screen.getByText(currentDate)).toBeInTheDocument();
});
