const prompt = require('prompt-sync')({ sigint: true });

// ------------------- *** -------------------

const str = String(prompt());

const arr = str.split(' ');

const stack = [];

for (let i = 0; i < arr.length; i++) {}

console.log(stack[0]);
