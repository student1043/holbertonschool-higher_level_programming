#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const completed = {};
request(url, function (error, response, body) {
  if (error) throw error;
  const data = JSON.parse(body);
  for (let i = 0; i < data.length; i++) {
    if (data[i].completed === true) {
      if (completed[data[i].userId]) {
        completed[data[i].userId] += 1;
      } else {
        completed[data[i].userId] = 1;
      }
    }
  }
  console.log(completed);
});
