function roadsBuilding(cities, roads) {
    'use strict';
    var newRoads = [];
    for(let i = 0; i < cities; i ++){
        for(let k = 0; k < cities; k++){
            if(!includesTuple([i,k], roads) && !includesTuple([i,k], newRoads) && i!=k){
                newRoads.push([i,k]);
            }
        }
    }
    return newRoads;
}

function includesTuple(tuple2, arr){
    if(arr.length == 0){
        return false;
    }
    return arr.reduce((a,b)=>{
        return a || (tuple2[0] == b[0] && tuple2[1] == b[1]) || (tuple2[1] == b[0] && tuple2[0] == b[1]);
    }, false);
}
