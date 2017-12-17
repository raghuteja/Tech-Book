```arbor
{
    "nodes": {
        "Data": {
            "color": "black"
        },
        "Architectures": {
            "color": "yellow"
        },
        "Lambda": {
            "color": "red"
        },
        "Kappa": {
            "color": "red"
        },
        "Lambda": {
            "color": "red"
        },
        "SummingBird": {
            "color": "red"
        }
    },
    "edges": {
        "Data": {
            "Architectures": {
                "color": "#b2b19d",
                "width": 2
            }
        },
        "Architectures": {
            "Lambda": {
                "color": "#b2b19d",
                "width": 2
            },
            "Kappa": {
                "color": "#b2b19d",
                "width": 2
            },
            "SummingBird": {
                "color": "#b2b19d",
                "width": 2
            }            
        }
    },
    "params": {
        "height": 600,
        "width": 300,
        "padding": [160,160,160,160]
    }
}
```