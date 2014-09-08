#!/bin/bash

git push origin
git checkout gh-pages
git checkout master -- candidates.json
git mv -f candidates.json _data/candidates.json
git commit
git push origin gh-pages
git checkout master
