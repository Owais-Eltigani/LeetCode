const prompt = require('prompt-sync')({ sigint: true });

function containDuplicate(arr) {
  const map = new Map();

  for (let i = 0; i < arr.length; i++) {
    if (map.has(arr[i])) {
      return true;
    }

    map.set(arr[i], 1);
  }

  return false;
}

function containDuplicate(arr, n) {
  for (let i = 0; i < n; i++) {
    for (let j = i + 1; j < n; j++) {
      if (arr[i] == arr[j]) {
        return true;
      }
    }
  }

  return false;
}

function inputArr(size) {
  const arr = [];

  for (let i = 0; i < size; i++) {
    arr.push(Number(prompt()));
  }

  return arr;
}

// ------------------- *** -------------------

let n = Number(prompt());

const arr = inputArr(n);

const result = containDuplicate(arr, n);

console.log(result);
