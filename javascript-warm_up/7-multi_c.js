#!/usr/bin/node
const argv = process.argv;
const number = Number(argv[2]);
const bool = isNaN(number);
if (typeof number === 'number' && bool === false) {
  for (let i = 0; i < number; i += 1) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
