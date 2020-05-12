#!/usr/bin/node
exports.converter = function (base) {
  return function (mybase) {
    return mybase.toString(base);
  };
};
