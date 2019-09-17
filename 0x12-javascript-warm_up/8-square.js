#!/usr/bin/node

const args = process.argv;

if (args[2] === undefined || isNaN(args[2])) {
  console.log('Missing size');
} else {
  for (let x = 0; x < args[2]; x++) {
    console.log('X'.repeat(args[2]));
  }
}
