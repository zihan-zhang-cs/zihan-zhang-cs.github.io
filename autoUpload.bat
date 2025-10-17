@echo off
REM 自动提交并推送更改脚本

REM 添加所有更改
git add .

REM 提交更改
git commit -m "upload a blong"

REM 推送到远程仓库
git push origin master

REM 提示推送完成
echo push success!
pause
