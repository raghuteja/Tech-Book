# Neural Network

House Price prediction: Using linear regression we can plot a straight line, As the house prices cannot be negative

{% graph %}
    {
        "title":"House Price Prediction",     
        "grid":true,
        "xAxis": {
            "label":"Size of House"
        },
        "yAxis": {
            "label":"Price"
        },
        "data": [
            { "fn": "x=y"},         
            { "fn": "(1+0.5cos(2*PI*x/100))"}
        ]
    }
{% endgraph %}