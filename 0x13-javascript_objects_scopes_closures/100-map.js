#!/usr/bin/node

const mapped = require('./100-data').list;

function newList (list) {
  console.log(list);

  const mo = list.map((val, idx) => idx * val);
  console.log(mo);
}

newList(mapped);
