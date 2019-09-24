#!/usr/bin/node

const obj = require('./101-data').dict;

const newDict = {};

for (const key in obj) {
  if (!(obj[key] in newDict)) {
    newDict[obj[key]] = [key];
  } else {
    newDict[obj[key]].push(key);
  }
}

console.log(newDict);
