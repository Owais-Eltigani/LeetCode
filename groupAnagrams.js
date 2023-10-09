const prompt = require('prompt-sync')({ sigint: true });

function inputArr(size) {
  const arr = [];

  for (let i = 0; i < size; i++) {
    arr.push(prompt());
  }

  return arr;
}

function unique(arr) {
  const set = new Set();

  for (let i = 0; i < arr.length; i++) {
    const str = arr[i].split('').sort().join('');

    set.add(str);
  }
  const myMap = new Map();

  let i = 0;

  set.forEach(value => {
    myMap.set(value, i++);
  });

  return myMap;
}

function group(arr) {
  const myMap = unique(arr);

  const dict = new Array(myMap.size);

  for (let i = 0; i < myMap.size; i++) {
    dict[i] = new Array();
  }

  for (let i = 0; i < arr.length; i++) {
    const temp = arr[i].split('').sort().join('');
    let j = myMap.get(temp);
    dict[j].push(arr[i]);
  }

  return dict;
}

// ------------------- *** -------------------

const size = Number(prompt());

const arr = inputArr(size);

console.log(group(arr));
