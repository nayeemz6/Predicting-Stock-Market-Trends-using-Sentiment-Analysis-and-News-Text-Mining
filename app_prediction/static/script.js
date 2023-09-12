// script.js
document.getElementById('sentimentForm').addEventListener('submit', function (event) {
    event.preventDefault();
    const inputText = document.getElementById('inputText').value;
    // Make AJAX call to your backend API for sentiment analysis
    // Update sentimentResult with the response
});
// Inside the AJAX call
fetch('/api/sentiment', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
    },
    body: JSON.stringify({ text: inputText }),
})
.then(response => response.json())
.then(data => {
    document.getElementById('sentimentResult').textContent = `Sentiment Score: ${data.score}`;
    // Make another AJAX call for prediction and update the chart
})
.catch(error => console.error('Error:', error));
