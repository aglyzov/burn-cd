#!/bin/sh

BIN=/usr/local/bin
DOC=/usr/local/share/burn-cd

cp -v burn-cd "$BIN"

mkdir ${DOC}
cp -v Changelog dotburn-cd.conf ${DOC}
