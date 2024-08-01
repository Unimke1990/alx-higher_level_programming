#!/usr/bin/node

const nums = process.argv[2];
const num = parseInt(nums);

if (!isNaN(num)){
console.log('My number: ' + num);} else{
console.log('Not a number');}
