#!/usr/bin/node
// process.argv
let i;
const argv = process.argv;
argv.forEach((val, index) => { i = index; });
if (i <= 3) {
  const myVar = argv[2] + ' is ' + argv[3];
  console.log(myVar);
}
