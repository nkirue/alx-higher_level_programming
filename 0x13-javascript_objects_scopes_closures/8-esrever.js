#!/usr/bin/node
exports.esrever = function (list) {
  let leng = list.length - 1;
  let k = 0;
  while ((leng - k) > 0) {
    const aux = list[leng];
    list[leng] = list[k];
    list[k] = aux;
    k++;
    leng--;
  }
  return list;
};
