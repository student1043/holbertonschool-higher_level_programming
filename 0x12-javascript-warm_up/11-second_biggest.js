#!/usr/bin/node
let first = 0; let second = 0;
if (process.argv.length <= 3) {
  console.log('0');
} else {
  for (let i = 0; i < process.argv.length; i++) {
    if (parseInt(process.argv[i]) > first) {
      second = first;
      first = parseInt(process.argv[i]);
    } else if (parseInt(process.argv[i]) > second && parseInt(process.argv[i]) < first) {
      second = parseInt(process.argv[i]);
    }
  }
  console.log(second);
}
