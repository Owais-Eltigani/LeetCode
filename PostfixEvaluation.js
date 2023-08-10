const prompt = require('prompt-sync')({ sigint: true });

// ------------------- *** -------------------

const str = String(prompt());

const arr = str.split(' ');

let i = 0;

while (arr.length > 1) {
  if (['+', '-', '*', '/'].some(elt => elt === arr[i])) {
    //
    const num1 = Number(arr.shift());
    const num2 = Number(arr.shift());
    const op = arr.shift();

    let result;

    switch (op) {
      case '+':
        result = num1 + num2;
        break;

      case '-':
        result = num1 - num2;
        break;

      case '/':
        result = num1 / num2;
        break;

      case '*':
        result = num1 * num2;
        break;
    }

    arr.unshift(result);
    i = 0;
  }
  i++;
}

console.log(arr[0]);
