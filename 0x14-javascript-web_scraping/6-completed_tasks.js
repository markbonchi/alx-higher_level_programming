#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, (err, res, body) => {
  if (err) {
    console.error(err);
  } else if (res.statusCode === 200) {
    const bodyJSON = JSON.parse(body);
    // console.log(bodyJSON);
    const tempList = {};
    for (const i in bodyJSON) {
      const task = bodyJSON[i];
      if (task.completed === true) {
        if (tempList[task.userId] === undefined) {
          tempList[task.userId] = 1;
        } else {
          tempList[task.userId]++;
        }
      }
    }
    console.log(tempList);
  } else {
    console.log(`Error code: ${res.statusCode}`);
  }
});
