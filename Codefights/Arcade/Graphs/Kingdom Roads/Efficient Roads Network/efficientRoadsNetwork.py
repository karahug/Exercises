def efficientRoadNetwork(n, roads):
    if n == 1:
        return True
    if len(roads) == 0:
        return False
    adjacencies = list(map(lambda x: [False] * n, range(n)))
    for road in roads:
        adjacencies[road[0]][road[1]] = True
        adjacencies[road[1]][road[0]] = True
    
    results = adjacencies[:]
    for i in range(n):
        for k in range(n):
            if(adjacencies[i][k]):
                results[i] = list(map(lambda x: x[0] or x[1], zip(results[i], adjacencies[k])))
    for i in range(n):
        for k in range(n):
            if(results[i][k] == False):
                return False
    return True

