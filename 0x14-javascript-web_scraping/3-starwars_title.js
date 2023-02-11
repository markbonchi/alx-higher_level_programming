#!/usr/bin/node
/* display the status code of a GET request.
*/

const request = require('request');
const API_URL = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(API_URL, (err, res, body) => {
  if (err) {
    console.error(err);
  } else if (res.statusCode === 200) {
    const responseJSON = JSON.parse(body);
    console.log(responseJSON.title);
  } else {
    console.log(`Error code: ${res.statusCode}`);
  }
});
