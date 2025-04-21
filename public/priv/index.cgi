#!/home/ugrad/24/s2410303/node-v22.13.1-linux-x64/bin/node

const fs = require('fs');
const stdin = process.stdin;
const envs = process.env;

process.stdout.write("Content-type: text/plain\r\n");
process.stdout.write("\r\n");
process.stdout.write(JSON.stringify({
    "env": envs,
    "stdin": stdin,
    "args": process.argv,
    "cwd": process.cwd(),
}, null, 4));
