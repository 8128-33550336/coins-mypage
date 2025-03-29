<?php

if ($_SERVER['REQUEST_METHOD'] != 'POST') {
    http_response_code(405);
    return;
}

$secret = file_get_contents('/home/ugrad/24/s2410303/.envs/gh_secret');
$body = file_get_contents('php://input');

$signature = 'sha256=' . hash_hmac('sha256', $body, $secret);

if ($_SERVER['HTTP_X_HUB_SIGNATURE_256'] != $signature) {
    http_response_code(403);
    return;
}

$dec_body = json_decode($body, true);
file_put_contents('/home/ugrad/24/s2410303/logs/deploy.log', $body, FILE_APPEND | LOCK_EX);

if ($_SERVER['HTTP_X_GITHUB_EVENT'] != 'release') {
    http_response_code(204);
    return;
}

if ($dec_body['action'] != 'created') {
    http_response_code(204);
    return;
}

$tag_name = $dec_body['release']['tag_name'];

print("Deploying {$tag_name}...\n");

print(`/home/ugrad/24/s2410303/pull_web.sh "{$tag_name}" 2>&1`);

http_response_code(201);
