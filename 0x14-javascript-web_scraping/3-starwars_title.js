#!/usr/bin/node

const args = process.argv.slice(2);

if (args.length === 1) {
  const request = require('request');
  const ep = args[0];
  const url = 'http://swapi.co/api/films/' + ep;

  request(url, function (err, response, body) {
    if (err) console.log(err);
    else if (response.statusCode === 200) {
      console.log(JSON.parse(body).title);
    }
  });
}
