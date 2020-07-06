#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(link, function (error, response, body) {
  if (error) throw error;
  const d = JSON.parse(body).characters;
  for (let i = 0; i < d.length; i++) {
    const mylink = d[i];
    request(mylink, function (error, response, body) {
      if (error) throw error;
      const d = JSON.parse(body);
      console.log(d.name);
    });
  }
});
