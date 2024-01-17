document.getElementById('submit-query').addEventListener('click', function() {
    var userInput = document.getElementById('natural-language-input').value;
    
    fetch('/generate_sql', { 
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ query: userInput }),
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('sql-output').value = data.sql;
        updateVisualization(data.sql);
    })
    .catch((error) => {
        console.error('Error:', error);
    });
});

function updateVisualization(data) {
    var visualizationDiv = document.getElementById('visualization');
    visualizationDiv.innerHTML = '<p>Chart would go here. Data: ' + data + '</p>';
    // Here you would integrate a chart library and pass the data to it
}
