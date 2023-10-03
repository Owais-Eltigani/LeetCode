const prompt = require('prompt-sync')();

function validAnagram(str1, str2) {
  if (str1.length !== str2.length) return false;

  const str_1 = str1.split('').sort();
  const str_2 = str2.split('').sort();

  for (let i = 0; i < str_1.length; i++) {
    if (str_1[i] !== str_2[i]) return false;
  }

  return true;
}

// ------------------- *** -------------------

const str1 = prompt();
const str2 = prompt();

const result = validAnagram(str1, str2);

console.log(result);
