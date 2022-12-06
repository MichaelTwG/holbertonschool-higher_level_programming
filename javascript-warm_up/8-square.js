#!/usr/bin/node
const argv = process.argv;
const number = Number(argv[2]);
const bool = isNaN(number);
let str = '';
if (typeof number === 'number' && bool === false) {
  for (let i = 0; i < number; i += 1) {
    for (let j = 0; j < number; j += 1) {
      str += 'x';
    }
    if (i < number - 1) {
      str += '\n';
    }
  }
  console.log(str);
} else {
  console.log('Missing size');
}
