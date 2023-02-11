#!/usr/bin/node

const fs = require('fs');
const request = require('request');
const API_URL = process.argv[2];
const file = process.argv[3];

request(API_URL, (err, res, body) => {
  if (err) {
    console.error(err);
  } else if (res.statusCode === 200) {
    fs.writeFile(file, body, 'utf-8', (err) => {
      if (err) throw (err);
    });
  } else {
    console.log(`Error code: ${res.statusCode}`);
  }
});
