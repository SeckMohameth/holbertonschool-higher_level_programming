#!/usr/bin/node

const args = process.argv.slice(2);

if (args.length === 2) {
  const fs = require('fs');
  const file = args[0];
  const data = args[1];

  fs.writeFile(file, data, 'utf-8', (err) => {
    if (err) console.log(err);
  });
}
