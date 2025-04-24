#!/home/ugrad/24/s2410303/node-v22.13.1-linux-x64/bin/node

const fs = require("fs");
const stdin = fs.readFileSync(0, "utf-8");
const envs = process.env;

process.stdout.write("Status: 200\r\n");
process.stdout.write("Content-type: application/json\r\n");
process.stdout.write("\r\n");
process.stdout.write(JSON.stringify({ stdin, envs, process }, null, 4) + "\n");
