#!/usr/bin/node

const url = 'http://swapi.co/api/films/' + process.argv[2];
const request = require('request');

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);
    for (const i of data.characters) {
      request(i, function (error, response, body) {
        if (error) {
          console.log(error);
        } else {
          const info = JSON.parse(body);
          console.log(info.name);
        }
      });
    }
  }
});
