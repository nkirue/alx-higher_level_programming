#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log('0');
} else {
  const ar = process.argv.slice(2).map(Number);
  const sec = ar.sort(function (x, y) { return y - x; })[1];
  console.log(sec);
}

