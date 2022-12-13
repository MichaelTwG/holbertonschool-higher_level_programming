#!/usr/bin/node
const fs = require('fs');
const args = process.argv;

const nameFile = args[2];
const string = args[3];

fs.writeFile(nameFile, string, { encoding: 'utf8' }, (err) => {
  if (err) {
    console.log(err);
  }
});
