tests = [{
    "input": {
        "cards": [10, 9, 8, 7, 6, 5, 4, 2, 1],
        "query": 6
    },
    "output": 4
}, {
    "input": {
        "cards": [29, 16, 14, 12, 10, 8, 7, 5, 2],
        "query": 8
    },
    "output": 5
}, {
    "input": {
        "cards": [29, 16, 10, 8, 7, 6, 5, 3, 2],
        "query": 10
    },
    "output": 2
}, {
    "input": {
        "cards": [27, 15, 9, 7, 6, 6, 4, 2, 1],
        "query": 1
    },
    "output": 8
}, {
    "input": {
        "cards": [27, 19, 16, 17, 15, 15, 14, 6, 1],
        "query": 19
    },
    "output": 1
}, {
    "input": {
        "cards": [12, 14, 6, 6, 6, 3, 3, 5, 5, 1],
        "query": 6
    },
    "output": 2
}]

large_tests = {
    "input": {
        "cards": list(range(10000000, 0, -1)),
        "query": 2
    },
    "output": 9999998
}
