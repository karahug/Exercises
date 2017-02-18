function shortestPathWithEdge(start, finish, weight, graph) {
    'use strict';
    const adjacencies = graph.map((a)=>{
                                  return a.slice();
                                  });
    const length = adjacencies.length;
    for(let n = 0; n < length; n++){
        for(let i = 0; i < length; i++){
            if(graph[n][i] != 0){
                for(let j = 0; j < length; j++){
                    const currentPath = adjacencies[n][j];
                    const potentialPath = adjacencies[n][i] + adjacencies[i][j];
                    if(adjacencies[i][j] != 0){
                        adjacencies[n][j] = currentPath == 0 && n!=j? potentialPath : Math.min(currentPath, potentialPath);
                    }
                }
            }
        }
    }
    var shortestPath = adjacencies[start - 1][finish - 1];
    for(let i = 0; i < length; i++){
        for(let j = 0; j < length; j++){
            if(graph[i][j] == 0 && i!=j){
                shortestPath = Math.min(shortestPath, adjacencies[start - 1][i] + adjacencies[j][finish - 1] + weight);
            }
        }
    }
    return shortestPath;
}
    