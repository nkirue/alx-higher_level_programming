#!/usr/bin/node
let nargi = 0;

exports.logMe = function (item) {
  console.log(nargi + ': ' + item);
  nargi++;
};
