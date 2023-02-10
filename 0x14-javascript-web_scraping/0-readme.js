#!/usr/bin/node
/* reads and prints the content of a file.
*/

const fs = require('fs');
const file = process.argv[2];

fs.readFile(file, 'utf-8', (err, fd) => {
  if (err){
    console.log(err);
  } else {
    console.log(fd);
  }
});

