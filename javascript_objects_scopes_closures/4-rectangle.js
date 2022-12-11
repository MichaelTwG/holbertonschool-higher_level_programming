#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let outStr = '';

    for (let i = 0; i < this.height; i += 1) {
      for (let j = 0; j < this.width; j += 1) {
        outStr += 'X';
      }
      if (i < this.height - 1) {
        outStr += '\n';
      }
    }
    console.log(outStr);
  }

  rotate () {
    const w = this.width;
    this.width = this.height;
    this.height = w;
  }

  double () {
    this.width = this.width * 2
    this.height = this.height * 2
  }
}

module.exports = Rectangle;
