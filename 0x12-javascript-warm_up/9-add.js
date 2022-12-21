#!/usr/bin/node
// process.argv

const argv = process.argv;
const add = (a, b) => { return parseInt(a) + parseInt(b); };
console.log(add(argv[2], argv[3]));
