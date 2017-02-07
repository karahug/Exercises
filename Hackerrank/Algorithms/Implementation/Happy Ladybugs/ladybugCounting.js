process.stdin.resume();
process.stdin.setEncoding('ascii');

var input_stdin = "";
var input_stdin_array = "";
var input_currentline = 0;

process.stdin.on('data', function (data) {
    input_stdin += data;
});

process.stdin.on('end', function () {
    input_stdin_array = input_stdin.split("\n");
    main();    
});

function readLine() {
    return input_stdin_array[input_currentline++];
}

/////////////// ignore above this line ////////////////////

function main() {
    var Q = parseInt(readLine());
    for(var a0 = 0; a0 < Q; a0++){
        var n = parseInt(readLine());
        var b = readLine();
        var result = null;
        if(b.includes('_')){
            var ladybugs = {};
            for(var i = 0; i < n; i++){
                var ladybug = b[i];
                if(ladybug != '_'){
                    ladybugs[ladybug] = ladybugs[ladybug] + 1 || 1;
                }
            }
            result = Object.keys(ladybugs).reduce(function(x,y){
                return x && ladybugs[y] > 1;
            }, true);
        } else{
            result = b.split('').reduce(function(total, value, index){
                return total && (value == b[index-1] || value == b[index + 1]);
            }, true);
        }
        console.log(result ? 'YES' : 'NO');
    }

}
