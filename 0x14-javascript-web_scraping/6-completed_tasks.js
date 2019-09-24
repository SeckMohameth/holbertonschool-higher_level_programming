#!/usr/bin/node

const args = process.argv.slice(2);

if (args.length === 1) {
  const request = require('request');
  const url = args[0];

  request(url, function (err, response, data) {
    if (err) console.log(err);
    else if (response.statusCode === 200) {
      const arr = JSON.parse(data);
      const list = {};
      for (let i = 0; i < arr.length; ++i) {
        if (!(arr[i].userId in list)) list[arr[i].userId] = 0;
        if (arr[i].completed === true) list[arr[i].userId] += 1;
      }
      console.log(list);
    }
  });
}
