#!/usr/bin/node
const fs = require('fs');
const request = require('request');
const url = process.argv[2];
request(url, function (error, response, body) {
  if (error) throw error;
  fs.writeFile(process.argv[3], response, 'utf-8', function (error, data) {
    if (error) {
      console.log(error);
    }
  });
});
