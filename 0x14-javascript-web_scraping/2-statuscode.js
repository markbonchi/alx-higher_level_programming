#!/usr/bin/node
/* display the status code of a GET request.
*/

const request = require('request');
const url = process.argv[2];

request(url, (err, res) => {
  if (err) {
    condole.error(err);  
  } else {
    console.log(`code: ${res.statusCode}`);
  }
});
