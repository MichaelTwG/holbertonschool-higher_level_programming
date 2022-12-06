#!/usr/bin/node
const argv = process.argv;
let number = Number(argv[2]);
if (argv.length === 2) {
  number = 1;
}
function factorial (n) {
  if (n === 0) {
    return 1;
  } else {
    return factorial(n - 1) * n;
  }
}
console.log(factorial(number));
