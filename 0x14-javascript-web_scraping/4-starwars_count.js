#!/usr/bin/node

const request = require('request');
const API_URL = process.argv[2];

request(API_URL, (err, res, body) => {
  if (err) {
    console.error(err);
  } else if (res.statusCode === 200) {
    const responseJSON = JSON.parse(body);
    // console.log(responseJSON.results)
    const result = responseJSON.results;
    let count = 0;
    result.forEach(element => {
      // console.log(element.characters);
      // element.forEach(value => {value == '/.\/18\/$/' ? i++ : i = i});
      const characters = element.characters;
      for (const indx in characters) {
        if (characters[indx].includes('18')) { count++; }
      }
    });
    console.log(count);
  } else {
    console.log(`Error code: ${res.statusCode}`);
  }
});
