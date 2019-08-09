'use strict';

const fs = require('fs');

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.replace(/\s*$/, '')
        .split('\n')
        .map(str => str.replace(/\s*$/, ''));

    main();
});

function readLine() {
    return inputString[currentLine++];
}

// Complete the isBalanced function below.
function isBalanced(str) {
    let stack = [];
    const braces = { '(': ')', '[': ']', '{': '}' }
    for (let char of str) {
        if (braces[char.valueOf()]) {
            stack.push(char)
        }
        else {
            if (stack.length === 0) {
                return 'NO';
            }
            else if (braces[stack[stack.length - 1].valueOf()] === char) {
                stack.pop()
            }
            else return 'NO';
        }
    }
    let output = stack.length === 0 ? 'YES' : 'NO';
    return output;

}

function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

    const t = parseInt(readLine(), 10);

    for (let tItr = 0; tItr < t; tItr++) {
        const s = readLine();

        let result = isBalanced(s);

        ws.write(result + "\n");
    }

    ws.end();
}

