#!/usr/bin/env bash

while read line; do
    key=`echo "$line" | cut -d '=' -f 1`
    val=`echo "$line" | cut -d '=' -f 2`
    find ./public -type f | xargs sed -i "s|{$key}|$val|g"
done < .env
