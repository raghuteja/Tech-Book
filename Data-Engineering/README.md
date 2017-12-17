```arbor
{
    "nodes": {
        "Data": {
            "color": "black"
        },
        "Architectures": {
            "color": "brown"
        },
        "File Systems": {
            "color": "brown"
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
        },
        "GFS": {
            "color": "red"
        },
        "HDFS": {
            "color": "red"
        },
        "Ceph File System": {
            "color": "red"
        },
        "Alluxio, Inc": {
            "color": "red"
        }
    },
    "edges": {
        "Data": {
            "Architectures": {
                "color": "#b2b19d",
                "width": 2
            },
            "File Systems": {
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
        },
        "File Systems": {
            "GFS": {
                "color": "#b2b19d",
                "width": 2
            },
            "HDFS": {
                "color": "#b2b19d",
                "width": 2
            },
            "Ceph File System": {
                "color": "#b2b19d",
                "width": 2
            },
            "Alluxio, Inc": {
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