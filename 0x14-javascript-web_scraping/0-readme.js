#!/usr/bin/node

const args = process.argv.slice(2);

if (args.length !== 1) {
    console.log('error');
} else {
    const fs = require('fs');
    fs.readFile(args[0], 'utf8', (err, data) => {
	if (err) console.log(err);
	else console.log(data);
    });
}
