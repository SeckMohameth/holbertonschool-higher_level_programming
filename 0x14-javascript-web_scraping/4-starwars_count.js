#!/usr/bin/node

const args = process.argv.slice(2);

if (args.length === 1) {
  const request = require('request');
  const url = args[0];

  request(url, function (err, response, data) {
    if (err) console.log(err);
    else if (response.statusCode === 200) {
      const results = (JSON.parse(data).results);
      let count = 0;
      const character = 'https://swapi.co/api/people/18/';
      for (let i = 0; i < results.length; i++) {
        const characters = results[i].characters;
        for (let j = 0; j < characters.length; ++j) {
          if (characters[j] === character) count += 1;
        }
      }
      console.log(count);
    }
  });
}
