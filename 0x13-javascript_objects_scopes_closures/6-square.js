#!/usr/bin/node
const SquareP = require('./5-square');

class Square extends SquareP {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let k = 0; k < this.height; k++) {
      let si = '';
      for (let l = 0; l < this.width; l++) {
        si += c;
      }
      console.log(si);
    }
  }
}

module.exports = Square;
