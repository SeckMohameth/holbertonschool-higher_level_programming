#!/usr/bin/node

const args = process.argv.slice(2);

if (args.length === 1) {
  const request = require('request');
  const url = args[0];

  request(url, function (err, response, body) {
    if (err) console.log(err);
    else console.log('code: ' + response.statusCode);
  });
}
