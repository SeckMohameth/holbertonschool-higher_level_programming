#!/usr/bin/node

exports.esrever = function (list) {
  const nl = [];
  while (list.length) {
    nl.push(list.pop());
  }
  return nl;
};
