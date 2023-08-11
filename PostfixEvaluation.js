const prompt = require('prompt-sync')({ sigint: true });

// ------------------- *** -------------------

const str = String(prompt());

const arr = str.split(' ');

const stack = [];

for (let i = 0; i < arr.length; i++) {
  if (['+', '-', '*', '/'].some(elt => elt === arr[i])) {
    //
    const num2 = Number(stack.pop());
    const num1 = Number(stack.pop());

    const op = arr[i];

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

    stack.push(Math.trunc(result));
  } else {
    stack.push(arr[i]);
  }
}

console.log(stack[0]);
