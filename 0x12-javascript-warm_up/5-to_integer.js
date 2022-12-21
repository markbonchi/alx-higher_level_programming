#!/usr/bin/node
// process.argv

const argv = process.argv;
const num = parseInt(argv[2]);
if (Number.isInteger(num)) {
  console.log(`My number: ${num}`);
} else {
  console.log('Not a number');
}
