const prompt = require('prompt-sync')({ sigint: true });

function twoSum(arr, target) {
  //

  if (arr.length < 2) return [-1];

  if (arr[0] + arr[arr.length - 1] === target) return [0, arr.length - 1];

  if (arr[0] + arr[arr.length - 1] < target)
    return twoSum(arr.slice(1), target);

  if (arr[0] + arr[arr.length - 1] > target)
    return twoSum(arr.slice(0, arr.length - 1), target);

  //
}

function twoSum2(arr, target) {
  //

  for (let i = 0; i < arr.length - 1; i++) {
    for (let j = i + 1; j < arr.length; j++) {
      if (arr[i] + arr[j] === target) return [i, j];
    }
  }

  //
}

function twoSum3(arr, target) {
  const map = new Map();

  for (let i = 0; i < arr.length; i++) {
    if (map.has(target - arr[i])) {
      return [map.get(target - arr[i]), i];
    }

    map.set(arr[i], i);
  }

  return [-1];
}

function inputArr(size) {
  const arr = [];

  for (let i = 0; i < size; i++) {
    arr.push(Number(prompt()));
  }

  return arr;
}

// ------------------- *** -------------------

const size = Number(prompt());

const arr = inputArr(size);

let target = Number(prompt());

const result = twoSum3(arr, target);

console.log(result);
