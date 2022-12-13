#!/usr/bin/node
const fs = require('fs');
const args = process.argv;

const fileName = './' + args[2];

fs.readFile(fileName, 'utf8', (err, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log(data.substring(0, data.length - 1));
  }
});
