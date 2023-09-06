document.addEventListener('DOMContentLoaded', () => {
  const getQuoteButton = document.getElementById('get-quote')
  const quoteText = document.getElementById('quote-text')

  getQuoteButton.addEventListener('click', () => {
    fetch('/get-quote')
      .then((response) => response.json())
      .then((data) => {
        quoteText.textContent = data.quote
      })
  })
})
