#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const args = process.argv;

const options = {
  url: args[2],
  method: 'GET',
  headers: {
    Accept: 'application/json'
  }
};

request(options, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    fs.writeFile(args[3], body, { encoding: 'utf8' }, (err) => {
      if (err) {
        console.log(err);
      }
    });
  }
});
