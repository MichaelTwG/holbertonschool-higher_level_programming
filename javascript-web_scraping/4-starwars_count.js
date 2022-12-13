#!/usr/bin/node
const request = require('request');
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
    const data = JSON.parse(body).results;
    const char = 'https://swapi-api.hbtn.io/api/people/18/';
    let count = 0;
    for (const res of data) {
      if (res.characters.includes(char)) {
        count += 1;
      }
    }
    console.log(count);
  }
});
