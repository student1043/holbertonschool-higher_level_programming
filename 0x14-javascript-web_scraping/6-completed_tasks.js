#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const completed = {};
request(url, function (error, response, body) {
  if (error) throw error;
  const d = JSON.parse(body);
  for (let i = 0; i < d.length; i++) {
    if (d[i].completed === true) {
      if (completed[d[i].userId]) {
        completed[d[i].userId] += 1;
      } else {
        completed[d[i].userId] = 1;
      }
    }
  }
  console.log(completed);
});
