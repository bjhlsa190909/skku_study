# 자주 사용되는 command
git add .
git status 
git commit -m "message"
git push
git pull
git merge main/test
git log --oneline --graph

# setup 
git config --global user.name "[firstname lastname]
git config --global user.email "[valid email]"

git config --global color.ui auto

git config --list

# git project 생성
cd [project path] 
git init(기존 디렉토리를 git 저장소로 만들기)
git add [file name.md]
git commit -m "first commit"
git branch -M main(Master branch -> main branch)
git remote add origin [git url]
git push -u origin main

git clone [url]




