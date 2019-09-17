#!/usr/bin/node

const args = process.argv;

if (isNaN(args[2])) {
  console.log('1');
} else {
  const num = fact(args[2]);
  console.log(num);
}

function fact (num) {
  if (num === 1) {
    return num;
  }
  return num * fact(num - 1);
}
