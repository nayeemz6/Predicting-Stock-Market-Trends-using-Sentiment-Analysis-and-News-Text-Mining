// Inside your AJAX success callback
const chartCanvas = document.getElementById('chart');
const ctx = chartCanvas.getContext('2d');
new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ['Label 1', 'Label 2', 'Label 3'], // Your labels
        datasets: [{
            label: 'Prediction Metrics',
            data: [value1, value2, value3], // Your values
            backgroundColor: ['rgba(75, 192, 192, 0.2)', ...], // Background colors
            borderColor: ['rgba(75, 192, 192, 1)', ...], // Border colors
            borderWidth: 1,
        }],
    },
});
