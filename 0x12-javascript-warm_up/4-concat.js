#!/usr/bin/node
// process.argv
let i;
let argv = process.argv;
argv.forEach((val, index) => { i = index; });
if (i <= 3) {
  let myVar = argv[2] + ' is ' + argv[3];
  console.log(myVar);
}
