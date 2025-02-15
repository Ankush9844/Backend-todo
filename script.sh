#!/bin/bash

rm -rf .git
git init
git add .
git config user.name "Ankush9844"
git config user.email "ankush.katkurwar30@gmail.com"
git commit -m "first commit"
git branch -M main
git remote add origin $1
git push -u origin main
