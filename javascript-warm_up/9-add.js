#!/usr/bin/node
const args = process.argv;
const number2 = Number(args[3]);
const number1 = Number(args[2]);
function add (a, b) {
  console.log(a + b);
}
add(number1, number2);
