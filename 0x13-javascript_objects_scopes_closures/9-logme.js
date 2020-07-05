#!/usr/bin/node
let i = 0;
exports.logMe = function (item) {
  function counter (i) {
    console.log(i + ': ' + item);
  }
  counter(i);
  i++;
};
