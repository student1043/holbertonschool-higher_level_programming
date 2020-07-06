#!/usr/bin/node
const process = require('process');
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (error) {
	console.log(error);
} else {
	const mylist = JSON.parse(body).results;
	let number = 0;
	for (const movie of mylist) {
		if (movie.characters.find(item => item.includes('/api/people/18/'))) {
			number++;
		}
	}
	console.log(number);
}
});
