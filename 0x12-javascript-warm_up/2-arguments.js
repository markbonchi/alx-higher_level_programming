#!/usr/bin/node
// print process.argv

let i;
process.argv.forEach((val, index) => { i = index; });
i > 2
  ? console.log('Arguments found')
  : i > 1
    ? console.log('Argument found')
    : console.log('No argument');
