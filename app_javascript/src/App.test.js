import { render, screen } from "@testing-library/react";
import App from "./App";

test("time is updated after page refresh", async () => {
  render(<App />);

  const timeElement = screen.getByTestId("time-element");
  const initialTime = timeElement.textContent;

  // Simulate page refresh
  window.location.reload();

  const newTime = timeElement.textContent;

  expect(newTime).not.toEqual(initialTime);
});
