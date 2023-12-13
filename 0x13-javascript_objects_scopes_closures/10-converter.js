#!/usr/bin/node

exports.converter = function (base) {
  return function (nom) {
    return nom.toString(base);
  };
};
