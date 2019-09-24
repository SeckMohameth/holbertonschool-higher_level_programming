#!/usr/bin/node

const args = process.argv.slice(2);

if (args.length === 2) {
  const request = require('request');
  const fs = require('fs');
  const url = args[0];
  const path = args[1];

  request(url, function (err, response, body) {
    if (err) console.log(err);
    else if (response.statusCode === 200) {
      fs.writeFile(path, body, 'utf-8', (err) => {
        if (err) console.log(err);
      });
    }
  });
}
