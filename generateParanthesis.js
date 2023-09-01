const prompt = require('prompt-sync')({ sigint: true });

function genratePara(stack, open, closed, limit, result = []) {
  if (open == limit && closed == limit) {
    result = [...result, stack.join('')];

    return result;
  }

  if (open < limit) {
    stack.push('(');
    result = genratePara(stack, open + 1, closed, limit, result);
    // stack.pop();
  }

  if (closed < open) {
    stack.push(')');
    result = genratePara(stack, open, closed + 1, limit, result);
    // stack.pop();
  }

  return result;
}

// ------------------- *** -------------------

let n = Number(prompt());

const stack = [];

const result = genratePara(stack, 0, 0, n);

console.log(result);
console.log(result.length);
