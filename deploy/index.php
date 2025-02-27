<?php

file_put_contents('~/logs/deploy3.log', '>>><<<', FILE_APPEND | LOCK_EX);

if ($_SERVER['REQUEST_METHOD'] != 'POST') {
    http_response_code(405);
    return;
}

$secret = file_get_contents('~/.envs/gh_secret');
$body = file_get_contents('php://input');

$signature = 'sha256=' . hash_hmac('sha256', $body, $secret);

file_put_contents('~/logs/deploy2.log', '>>>' . $body . '<<<' . $signature . '>>>' . $_SERVER['HTTP_X-HUB-SIGNATURE-256'] . '<<<' . $_SERVER['HTTP_X-Hub-Signature-256'] . '>>>', FILE_APPEND | LOCK_EX);

if ($_SERVER['HTTP_X-HUB-SIGNATURE-256'] != $signature) {
    http_response_code(403);
    return;
}

$dec_body = json_decode($body, true);
file_put_contents('~/logs/deploy.log', $body, FILE_APPEND | LOCK_EX);

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
