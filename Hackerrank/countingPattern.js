function getNextRun(s){
    var length = 0;
    var l = s.length;
    var type = s[l-1]
    for(let i = 0; i < l; i++){
        nextChar = s[l - i -1];
        if(nextChar == type){
            s.pop()
            length++;
        }else{
            
            return length;
        }
    }
    return length;
}
function counting(s) {
    var a = s.split('');
    var l = a.length;
    var count = 0;
    var run1 = getNextRun(a);
    if(run1 == l){
        return 0;
    }
    var run2 = {};
    while(a.length != 0){
        //find run2.type, length
        run2 = getNextRun(a);
        count += Math.min(run1, run2)
        run1 = run2;
    }
    return count;
}
