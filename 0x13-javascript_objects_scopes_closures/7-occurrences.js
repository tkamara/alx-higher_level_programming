#!/usr/bin/node

// function that returns number of occurrences in list

exports.nbOccurences = function (list, searchElement) {
  let num = 0;
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      num += 1;
    }
  }
  return num;
};
