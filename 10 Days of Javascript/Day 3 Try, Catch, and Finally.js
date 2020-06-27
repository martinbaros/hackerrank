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

/*
 * Complete the reverseString function
 * Use console.log() to print to stdout.
 */
function reverseString(s) {
    let aktual = s
    let neue
    try{
        let arr = s.split("")
        let reverse_arr = arr.reverse();
        neue = reverse_arr.join("")
    }catch(e){
        console.log(e.message);
        neue = aktual
    }finally{
        console.log(neue)
    }

}


function main() {
    const s = eval(readLine());

    reverseString(s);
}
