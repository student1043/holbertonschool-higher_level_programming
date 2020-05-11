#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0) {
    } else if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
      this.print = function () {
        let str = '';
        for (let i = 0; i < h; i++) {
          for (let j = 0; j < w; j++) { str += 'X' + ''; }
          if (i < w) { str += '\n'; }
        }
        console.log(str);
      };
    }
  }
}
module.exports = Rectangle;
