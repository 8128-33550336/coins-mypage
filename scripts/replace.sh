#!/usr/bin/env bash

while read line; do
    key=`echo "$line" | cut -d '=' -f 1`
    val=`echo "$line" | cut -d '=' -f 2`
    find ./public -type f | xargs -I F -n 1 sed -i "s|{$key}|$val|g" F
done < .env.template
