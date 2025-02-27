<?php

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    http_response_code(405);
    return;
}

$secret = file_get_contents('../.envs/gh_secret');
$body = file_get_contents('php://input');

$signature = 'sha256=' . hash_hmac('sha256', $body, $secret);

if ($_SERVER['HTTP_X-HUB-SIGNATURE-256'] != $signature) {
    http_response_code(403);
    return;
}

$dec_body = json_decode($body, true);
file_put_contents('~/deploy.log', $body, FILE_APPEND | LOCK_EX);

if ($dec_body['action'] != 'push') {
    http_response_code(204);
    return;
}

if ($dec_body['action'] != 'push') {
    http_response_code(204);
    return;
}

if ($dec_body['ref'] != 'refs/heads/main') {
    http_response_code(204);
    return;
}

exec('~/pull_web.sh');
