#!/usr/bin/node
const request = require('request');
const args = process.argv;

const options = {
  url: args[2],
  method: 'GET',
  headers: {
    accept: 'application/json'
  }
};

request(options, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    const data = JSON.parse(body);
    const tCopleted = [];
    const ids = [];
    const returnObj = {};

    for (const task of data) {
      if (task.completed) {
        tCopleted.push(task);
        if (ids.includes(task.userId) !== true) {
          ids.push(task.userId);
        }
      }
    }
    let count = 0;
    for (const id of ids) {
      count = 0;
      for (const t of tCopleted) {
        if (t.userId === id) {
          count += 1;
        }
      }
      returnObj[id.toString()] = count;
    }
    console.log(returnObj);
  }
});
