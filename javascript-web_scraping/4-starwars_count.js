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
    let count = 0;

    for (const res of data) {
      for (const c of res.characters) {
        const id = c.split('/')[5];
        if (id === '18') {
          count += 1;
        }
      }
    }
    console.log(count);
  }
});
