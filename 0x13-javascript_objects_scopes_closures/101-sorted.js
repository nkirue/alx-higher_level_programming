#!/usr/bin/node
const dict = require('./101-data').dict;

const ttalist = Object.entries(dict);
const valsi = Object.values(dict);
const valsiUniq = [...new Set(valsi)];
const newDict = {};
for (const j in valsiUniq) {
  const list = [];
  for (const k in ttalist) {
    if (ttalist[k][1] === valsiUniq[j]) {
      list.unshift(ttalist[k][0]);
    }
  }
  newDict[valsiUniq[j]] = list;
}
console.log(newDict);
