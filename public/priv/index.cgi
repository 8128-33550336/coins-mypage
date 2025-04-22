#!/home/ugrad/24/s2410303/node-v22.13.1-linux-x64/bin/node

const fs = require('fs');
const stdin = fs.readFileSync(0, 'utf-8');
const envs = process.env;

const token = envs['HTTP_CF_TURNSTILE_RESPONSE'] || '';

const checkToken = (token) => {
    const tokenParts = token.split(' ');
    if (tokenParts.length !== 2 || tokenParts[0] !== 'Bearer') {
        return false;
    }
    const tokenValue = tokenParts[1];

    return tokenValue === 'your_secret_token';
};

if (!checkToken(token)) {
    process.stdout.write("Status: 401\r\n");
    // process.stdout.write("\r\n");
    // process.exit(0);
} else {
    process.stdout.write("Status: 200\r\n");
}

process.stdout.write("Content-type: application/json\r\n");
process.stdout.write("Access-Control-Allow-Origin: null\r\n");
process.stdout.write("Cache-Control: no-store\r\n");
process.stdout.write("\r\n");
process.stdout.write(JSON.stringify({
    "env": envs,
    "stdin": stdin,
    "args": process.argv,
    "cwd": process.cwd(),
}, null, 4));
