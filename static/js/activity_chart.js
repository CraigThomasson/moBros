function renderActivityChart(totalCompletedActivities, totalSessions, activitiesByDifficulty) {
    var ctx = document.getElementById('activityChart').getContext('2d');
    
    var difficultyLabels = activitiesByDifficulty.map(function(difficulty) {
        return 'Difficulty ' + difficulty.difficulty;
    });
    var difficultyCounts = activitiesByDifficulty.map(function(difficulty) {
        return difficulty.total;
    });

    var chartData = {
        labels: difficultyLabels,
        datasets: [{
            label: 'Number of Activities',
            data: difficultyCounts,
            backgroundColor: 'rgba(54, 162, 235, 0.2)',
            borderColor: 'rgba(54, 162, 235, 1)',
            borderWidth: 1
        }]
    };

    var chartOptions = {
        scales: {
            y: {
                beginAtZero: true
            }
        },
        plugins: {
            title: {
                display: true,
                text: 'Activities Completed at Each Difficulty Level'
            }
        }
    };

    var myChart = new Chart(ctx, {
        type: 'bar',
        data: chartData,
        options: chartOptions
    });
}
