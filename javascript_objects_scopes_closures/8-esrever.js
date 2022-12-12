#!/usr/bin/node

exports.esrever = function (list) {
  const reversedList = [];

  let len = list.length - 1;

  while (len >= 0) {
    reversedList.push(list[len]);
    len = len - 1;
  }
  return reversedList;
};

const esrever = require('./8-esrever').esrever;
console.log(esrever([1, 2, 3, 4, 5]));
