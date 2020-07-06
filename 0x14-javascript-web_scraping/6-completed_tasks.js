#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const completed = {};
request(link, function (error, response, body) {
  if (error) { console.log(error); }
  const mydata = JSON.parse(body);
  for (let i = 0; i < mydata.length; i++) {
    if (mydata[i].completed === true) {
      if (completed[mydata[i].userId]) {
        completed[mydata[i].userId] += 1;
      } else {
        completed[mydata[i].userId] = 1;
      }
    }
  }
  console.log(completed);
});