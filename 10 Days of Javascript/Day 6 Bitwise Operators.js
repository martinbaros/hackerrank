'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(string => {
        return string.trim();
    });

    main();
});

function readLine() {
    return inputString[currentLine++];
}


function getMaxLessThanK(n,k){
    let maxo = 0
    for (let i=1; i<=n; ++i){
        for (let q=i+1; q<=n; ++q){
            let vys = i & q;
            if (vys<k){
                if (vys > maxo){
                    maxo = vys
                }
            }
        }
    }
    return maxo;
}



function main() {
    const q = +(readLine());

    for (let i = 0; i < q; i++) {
        const [n, k] = readLine().split(' ').map(Number);

        console.log(getMaxLessThanK(n, k));
    }
}
