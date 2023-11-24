function renderActivityChart(activityDates, activityCounts) {
    var ctx = document.getElementById('activityChart').getContext('2d');
    var chart = new Chart(ctx, {
        type: 'bar',  // Changed from 'line' to 'bar'
        data: {
            labels: activityDates,
            datasets: [{
                label: 'Completed Activities',
                data: activityCounts,
                backgroundColor: 'rgba(0, 123, 255, 0.5)',  // Example color, adjust as needed
                borderColor: 'rgba(0, 123, 255, 1)',
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
}
