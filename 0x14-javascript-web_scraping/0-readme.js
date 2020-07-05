#!/usr/bin/node
const fs = require('fs');
fs.readFile(process.argv[2], 'utf8', function read (err, data) {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
