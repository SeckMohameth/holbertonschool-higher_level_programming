#!/usr/bin/node

const args = process.argv;

args.splice(0, 2);

let second = 0;

if (args.length <= 3) {
  console.log(0);
} else {
  args.sort();
  second = args[args.length - 2];
  console.log(second);
}
