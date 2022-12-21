#!/usr/bin/node
// print process.argv

let i;
process.argv.forEach((val, index) => { i = index; });
i < 2 ? console.log('No argument') : console.log('Argument found');
