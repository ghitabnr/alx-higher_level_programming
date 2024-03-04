#!/usr/bin/node

const fs = require('fs');

const [, , fileA, fileB, fileC] = process.argv;

// Read contents of fileA
fs.readFile(fileA, 'utf8', (err, dataA) => {
  if (err) throw err;

  // Read contents of fileB
  fs.readFile(fileB, 'utf8', (err, dataB) => {
    if (err) throw err;

    // Concatenate data from fileA and fileB
    const concatenatedData = `${dataA}${dataB}`;

    // Write concatenated data to fileC
    fs.writeFile(fileC, concatenatedData, (err) => {
      if (err) throw err;
      console.log(`The content of ${fileA} and ${fileB} has been concatenated and saved to ${fileC}`);
    });
  });
});