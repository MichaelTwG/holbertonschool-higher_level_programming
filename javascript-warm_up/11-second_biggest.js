#!/usr/bin/node
const args = process.argv;
const numbers = [];
if (args[2] === '1' && args.length < 4) {
  console.log(0);
} else if (args.length < 3) {
  console.log(0);
} else {
  for (let i = 2; i < args.length; i += 1) {
    numbers.push(Number(args[i]));
  }
  const maxNum = Math.max(...numbers);
  const index = numbers.indexOf(maxNum);
  numbers.splice(index, 1);
  console.log(Math.max(...numbers));
}
