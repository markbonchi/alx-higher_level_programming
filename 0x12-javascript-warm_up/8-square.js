#!/usr/bin/node
// process.argv

const argv = process.argv;
const num = parseInt(argv[2]);
if (Number.isInteger(num)) {
  let string;
  for (let i = 0; i < num; i++) {
    if (i === 0) {
      string = 'X';
      continue;
    }
    string += 'X';
  }
  for (let i = 0; i < num; i++) console.log(string);
} else {
  console.log('Missing size');
}
