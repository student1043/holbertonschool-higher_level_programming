#!/usr/bin/node
if (!parseInt(process.argv[2])) {
  console.log('Missing size');
} else {
  const x = parseInt(process.argv[2]);
  let str = '';
  for (let i = 0; i < x; i++) {
    for (let j = 0; j < x; j++) { str += 'X' + ''; }
    if (i < x - 1) { str += '\n'; }
  }
  console.log(str);
}
