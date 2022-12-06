#!/usr/bin/node
const argv = process.argv;
const number = Number(argv[2]);
const bool = isNaN(number);
if (typeof number === 'number' && bool === false) {
  console.log('My number: ' + number);
} else {
  console.log('Not a number');
}
