#/bin/bash

cd .config/nvim
git add .
git commit -m "update sth"
git push

cd ../../private
git add .
git commit -m "update sth"
git push

cd ..
git add .
git commit -m "update sth"
git push origin arch-xfce

