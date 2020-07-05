#!/usr/bin/node
function myfactorial (number) {
  if (number <= 0) {
    return 1;
  } else {
    return (number * myfactorial(number - 1));
  }
}
console.log(myfactorial(parseInt(process.argv[2]) || 1));
