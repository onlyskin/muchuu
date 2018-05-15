#!/bin/bash

TSC=node_modules/typescript/bin/tsc
BROWSERIFY=node_modules/browserify/bin/cmd.js

mkdir -p out
mkdir -p static

$TSC 
$BROWSERIFY -o out/app.bundle.js out/app.js

cp out/app.bundle.js static/app.bundle.js
