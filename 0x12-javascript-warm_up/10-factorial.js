#!/usr/bin/node
// process.argv

const argv = process.argv;
function factorial (i) {
  if (parseInt(i) <= 1 || !Number.isInteger(parseInt(i))) {
    return 1;
  }
  return parseInt(i) * factorial(parseInt(i) - 1);
}

console.log(factorial(argv[2]));
