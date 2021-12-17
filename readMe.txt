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
