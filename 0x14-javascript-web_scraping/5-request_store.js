#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
request(url, function (error, response, body) {
<<<<<<< HEAD
	if (error) {
		console.log(error);
	} else {
		fs.writeFile(process.argv[3], body, 'utf8', function (error, data) {
			if (error) {
				console.log(error);
			}
		});
	}
});
=======
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(process.argv[3], body, 'utf8', (error) => {
      if (error) { console.log(error); }
    });
  }
});
>>>>>>> c77e38429474e5c4c4ceb66bba1b23a7d0717946
