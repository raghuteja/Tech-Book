```arbor
{
  "nodes": {
    "Machine Learning": {
      "color": "black"
    },
    "Supervised Learning": {
      "color": "red"
    },
    "Semi-Supervised Learning": {
      "color": "red"
    },
    "Unsupervised Learning": {
      "color": "red"
    }
  },
  "edges": {
    "Machine Learning": {
      "Supervised Learning": {
        "color": "#b2b19d",
        "width": 2,
        "directed": true
      },
      "Semi-Supervised Learning": {
        "color": "#b2b19d",
        "width": 2,
        "directed": true
      },
      "Unsupervised Learning": {
        "color": "#b2b19d",
        "width": 2,
        "directed": true
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