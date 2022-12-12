#!/usr/bin/node

const sQ = require('./5-square');
class Square extends (sQ) {
  constructor (size) {
    super(size);
  }

  charPrint (c) {
    let outStr = '';

    for (let i = 0; i < this.height; i += 1) {
      for (let j = 0; j < this.width; j += 1) {
        if (c) {
          outStr += c;
        } else {
          outStr += 'X';
        }
      }
      if (i < this.height - 1) {
        outStr += '\n';
      }
    }
    console.log(outStr);
  }
}

module.exports = Square;
