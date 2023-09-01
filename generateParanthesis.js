const prompt = require('prompt-sync')({ sigint: true });

function genratePara(stack, open, closed, limit, result = []) {
  if (open == limit && closed == limit) {
    result = [...result, stack.join('')];

    return result;
  }

  if (open < limit) {
    stack.push('(');
    result = genratePara(stack, open + 1, closed, limit, result);
    stack.pop();
  }

  if (closed < open) {
    stack.push(')');
    result = genratePara(stack, open, closed + 1, limit, result);
    stack.pop();
  }

  return result;
}

function solve2(stack, open, closed, limit, result = []) {
  if (stack.length == limit * 2) {
    result.push(stack);
    return result;
  }

  if (open < limit) {
    // stack.push('(');
    solve2(stack + '(', open + 1, closed, limit, result);
  }

  if (closed < open) {
    // stack.push(')');
    solve2(stack + ')', open, closed + 1, limit, result);
  }

  return result;
}

// ------------------- *** -------------------

let n = Number(prompt());

const stack = [];

const result = solve2(stack, 0, 0, n);

console.log(result);
// console.log(result.length);
