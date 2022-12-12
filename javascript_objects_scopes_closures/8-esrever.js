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
