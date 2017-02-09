function stringsRearrangement(ia) {
    'use strict';
    var adj = ia.map(function(v1){
        var av = ia.map(function(v2,k){
            var c = v1.split('').reduce((a,b,i)=>{return a + ((b === v2[i])? 0:1)}, 0);
            return c === 1;
        });
        return av;
    });
    var vs = [];
    const n = ia.length;
    for(let i = 0; i < n; i++){
        vs[i] = [];
        for(let j = 0; j < 1<<n; j++){
            vs[i][j] = false;
        }
    }
    for(let i = 0; i < n; i++){
        vs[i][1 << i] = true;
    }
    for(let j = 0; j < 1 << n; j++){
        for(let i = 0; i < n; i++){
            if(j & (1<<i)){
                for(let k = 0; k < n; k++){
                    if(i != k && ((1<<k)&j) && adj[i][k] && (vs[k][(1<<i)^j] === true)){
                        vs[i][j] = true;
                        break;
                    }
                }
            }
        }
    }
    for(let i = 0; i < n; i++){
        if(vs[i][(1 << n) - 1]){
            return true;
        }
    }
    return false;
}
