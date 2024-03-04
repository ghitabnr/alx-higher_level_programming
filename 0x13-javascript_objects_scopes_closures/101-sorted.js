#!/usr/bin/node

const { dict } = require('./101-data');

const invertedDict = {};
for (const key in dict) {
  const value = dict[key];
  if (!invertedDict[value]) {
    invertedDict[value] = [key];
  } else {
    invertedDict[value].push(key);
  }
}

console.log(invertedDict);