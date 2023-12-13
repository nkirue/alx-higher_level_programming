#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let k = 0; k < this.height; k++) {
      let si = '';
      for (let l = 0; l < this.width; l++) {
        si += 'X';
      }
      console.log(si);
    }
  }

  rotate () {
    const auxi = this.width;
    this.width = this.height;
    this.height = auxi;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
