#!/usr/bin/node
const process = require('process');
const request = require('request');
request(process.argv[2], function (error, response, body) {
	if (error) {
		console.log(error);
	  }
	const userdata = JSON.parse(body);
	const uname = userdata.characters;
	console.log(uname);
});
