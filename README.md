# security

安装git
=========================================
Debian/Ubuntu
For the latest stable version for your release of Debian/Ubuntu
# apt-get install git

卸载git
=============================
# sudo apt-get autoremove --purge <softname>
sudo ———— 获取 root 权限
apt-get ——— 执行安装卸载功能的软件
autoremove — 告诉 apt-get 我们所要做的操作是移除软件
--purge ——— 注意这前面是两个短划线，这个参数是告诉他们要完整的干净的彻底的移除。


连接github
=============================
# git config --global user.name "zhangbin0git"
# git config --global user.email "zhangbin.email@foxmail.com"
# ssh-keygen -t rsa -C "zhangbin.email@foxmail.com"
# ssh -T git@github.com

连接github远程仓库
==================================
# echo "# security" >> README.md
# git init
# git add README.md
# git commit -m "first commit"
# git remote add origin git@github.com:zhangbin0git/security.git
# git push -u origin master

配置.gitignore
===========================
GitHub已经为我们准备了各种.gitignore配置文件，只需要组合一下就可以使用了 https://github.com/github/gitignore

eg：
---------------------------------
# Windows:
Thumbs.db
ehthumbs.db
Desktop.ini

# Python:
*.py[cod]
*.so
*.egg
*.egg-info
dist
build

# My configurations:
db.ini
deploy_key_rsa
---------------------------------

你发现，可能是.gitignore写得有问题，需要找出来到底哪个规则写错了，可以用git check-ignore命令检查
# git check-ignore -v App.class

git 配置别名
================
# git config --global alias.st status
# git config --global alias.co checkout
# git config --global alias.ci commit
# git config --global alias.br branch
命令git reset HEAD file可以把暂存区的修改撤销掉（unstage），重新放回工作区
# git config --global alias.unstage 'reset HEAD'
配置一个git last，让其显示最后一次提交信息
# git config --global alias.last 'log -1'
# git lg
# git config --global alias.lg "log --color --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit"

添加git config配置
=================================
增
# git config --global 命名 '值';
改:
如果这个命名存在也可以直接覆盖修改,还可以替换git config中已有的邮箱
# git config --global --replace-all user.email "输入你的邮箱"
# git config --global --replace-all user.name "输入你的用户名"
删除
# git config   --global --unset  命名



～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～
# 相关问题
～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～
git [packet_write_wait connection to xx.xx.xx.xx Broken pipe]解决办法
============================
找到git安装的目录/etc/ssh，打开ssh_config文件，在其中修改（或者添加）

Host *  ---->Host在上图中找到
ServerAliveInterval 120


ssh 调试
==============================
运用shh -T -v git@github.com查看具体出错信息，再根据信息来调试































