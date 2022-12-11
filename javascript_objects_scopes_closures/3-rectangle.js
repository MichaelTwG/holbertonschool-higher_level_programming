#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print() {

    let out_str = '';

    for (let i = 0; i < this.height; i += 1) {

      for (let j = 0; j < this.width; j += 1) {
        out_str += 'X';
      }
      if (i < this.height - 1) {
        out_str += '\n';
      }
    }
    console.log(out_str);
  }
}

module.exports = Rectangle;
