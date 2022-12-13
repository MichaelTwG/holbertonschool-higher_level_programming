#!/usr/bin/node
const request = require('request');
const args = process.argv;

const url = 'https://swapi-api.hbtn.io/api/films/' + args[2];

const options = {
  url: url,
  method: 'GET',
  headers: {
    Accept: 'application/json'
  }
};

request(options, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    const data = JSON.parse(body);
    console.log(data.title);
  }
});
