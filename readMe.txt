1、生成数据库bdrs,根据table.sql生成表

2、执行CatchMe.py，读取页面、写入文件，读取文件并写入数据库；

3、执行db_connect.py 可显示词云

安装词云对应的命令。
pip install numpy matplotlib pillow wordcloud imageio jieba snownlp itchat -i https://pypi.tuna.tsinghua.edu.cn/simple





==零散记录====================================


1、进度条包：tqdm
2、main方法要写在 方法的下面才能调用。
3、配置Anaconda3
3.1、cmd显示：
  查看版本： conda --version
3.2、更新： conda udpate --all
       conda upgrade --all
3.3、idea 集成Anaconda3
project structure->project ->new >新增Anaconda3对应的sdk
modules 选择sdk
最后重启
4、安装某个包：project structure-》platform settings ->sdks->package->搜索-》install
5、idea 配置github
git config --global user.name "Your Name"
git config --global user.email "email@example.com"

File-->Setting->Version Control-->Git-->Path to Git executable选择你的git安装后的git.exe文件，然后点击Test，测试是否设置成功
github 获取token登陆：
参考文章连接：https://blog.csdn.net/u014175572/article/details/55510825/
生成token的快捷链接：https://github.com/settings/tokens
 头像-》settings->Developer Settings->Personal access tokens->生成。
note描述，下面全部勾选权限。

github上传：
git命令上传：
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/garyHelloDev/python_test.git
git push -u origin main

ssh配置：
参考：https://docs.github.com/cn/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account
检查
ls -al ~/.ssh


生成
ssh-keygen -t ed25519 -C "yourexample@xx.com"

Your public key has been saved in /c/Users/xx/.ssh/id_ed25519.pub
C:\Users\xx\.ssh\id_ed25519.pub

#添加
pbcopy < ~/.ssh/id_ed25519.pub 或者直接打开
到github settings->ssh and gpg keys->new ssh keys 粘贴上
