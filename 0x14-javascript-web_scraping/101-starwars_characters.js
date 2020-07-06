#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(url, function (error, response, body) {
  if (error) throw error;
  const d = JSON.parse(body).characters;
  printChars(d, 0);
});

function printChars (characters, index) {
  request(chars[index], function (error, response, body) {
    if (error) throw error;
    console.log(JSON.parse(body).name);
    if (index + 1 < characters.length) {
      printChars(characters, index + 1);
    }
  });
}
