const prompt = require('prompt-sync')({ sigint: true });

function check(s) {
  if (s == '(' || s == '[' || s == '{') return true;

  return false;
}

function isValid(stack, str) {
  if (stack.length == 0) return false;

  if (
    (stack.at(-1) == '(' && str == ')') ||
    (stack.at(-1) == '[' && str == ']') ||
    (stack.at(-1) == '{' && str == '}')
  ) {
    stack.pop();
    return true;
  }

  return false;
}

// ---------- Problem 20: Valid Parentheses ---------- //

const str = prompt();
const stack = [];

const arr = str.split('');

let status = true;

for (let i = 0; i < arr.length; i++) {
  if (check(arr[i])) {
    stack.push(arr[i]);
  } else {
    if (!isValid(stack, arr[i])) {
      status = false;
      break;
    }
  }
}

if (status && stack.length == 0) console.log(status);
else console.log(false);
