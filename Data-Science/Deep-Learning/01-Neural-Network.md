# Neural Network

House Price prediction: Using linear regression we can plot a straight line, As the house prices cannot be negative

{% graph %}
    {
        "title":"cos(2*PI*x/2)*(1+0.5cos(2*PI*x/100))",     
        "grid":true,
        "xAxis": {
            "label":"Sample",
            "domain": [0,300]
        },
        "yAxis": {
            "label":"Amplitude",
            "domain": [-1.5,1.5]
        },
        "data": [
            { "fn": "cos(2*PI*x/2)*(1+0.5cos(2*PI*x/100))"},         
            { "fn": "(1+0.5cos(2*PI*x/100))"}
        ]
    }
{% endgraph %}