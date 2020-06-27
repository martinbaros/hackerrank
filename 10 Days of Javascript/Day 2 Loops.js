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
 * Complete the vowelsAndConsonants function.
 * Print your output using 'console.log()'.
 */
function vowelsAndConsonants(s) {
    let vove = ["a", "e", "i", "o", "u"]
    let ostatok = []
    for (let vow of s){
        if (vove.includes(vow)){
            console.log(vow)
        }
        else{
            ostatok.push(vow)
        }
    }
    for (let vow of ostatok){console.log(vow)}

}


function main() {
    const s = readLine();

    vowelsAndConsonants(s);
}
