#!/usr/bin/node
/* display the status code of a GET request.
*/

const https = require('https');
const url = process.argv[2];

https.get(url, (res) => {
  console.log(`code: ${res.statusCode}`);
});
