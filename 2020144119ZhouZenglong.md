# **Git原理与基本使用**

## 1 Git和Github

　　指定了remote链接和用户信息（git靠用户名+邮箱识别用户）之后，git可以帮你将提交过到你本地分支的代码push到**远程的git仓库**（任意提供了git托管服务的服务器上都可以，包括你**自己建一个服务器** 或者 **GitHub/BitBucket等网站提供的服务器**）或者将远程仓库的代码 fetch 到本地。

　　**Github只是一个提供存储空间的服务器，用来存储git仓库**。当然现在Github已经由一个存放git仓库的网站空间发展为了一个开源社区（**不只具有存储git仓库的功能了**），你可以参与别人的开源项目，也可以让别人参与你的开源项目。

### 2 Git结构

先不看远程服务器，只关注自己的本地电脑。git的使用过程如下：

![img](https://img-blog.csdnimg.cn/20190331145807855.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FpbnNoaTk2NTI3MzEwMQ==,size_16,color_FFFFFF,t_70)

## 3 创建版本库

### 3.1创建一个空目录（最好不要包含中文）

$ mkdir mymenu
$ cd mymenu
$ pwd
/Users/hxk/mymenu
pwd命令显示当前目录

### 3.2初始化仓库

git init命令把这个目录变成git可以管理的仓库

$ git init
Initialized empty Git repository in /Users/hxk/mymenu/.git/
初始化了一个空的仓库，目录下多了.git目录

系统自动创建了唯一一个master分支

版本控制系统只能跟踪文本文件的改动，且编码方式是utf-8

## 4 文件的基本操作

创建一个test.txt文件，内容如下：

Hello World

### 4.1添加文件到仓库

$ git add test.txt

### 4.2提交文件到仓库

$ git commit -m "a new file"
-m后面输入的是本次提交的说明，提交成功后会显示：

1 file changed：1个文件被改动（我们新添加的readme.txt文件）；

2 insertions：插入了两行内容（readme.txt有两行内容）。

为什么Git添加文件需要add，commit一共两步呢？因为commit可以一次提交很多文件，所以你可以多次add不同的文件

$ git add file1.txt
$ git add file2.txt file3.txt
$ git commit -m "add 3 files."
如果提交的备注写错了，可以用以下命令修改刚刚提交的备注

$ git commit --amend

### 4.3修改文件

将test.txt文件修改如下：

Hello World ABC
提交

$ git add test.txt
$ git commit -m "append ABC"
每次commit都会生成一个“快照”

### 4.4查看历史记录

$ git log
commit 1094adb7b9b3807259d8cb349e7df1d4d6477073 (HEAD -> master)
Author: hxk <hxk@gmail.com>
Date:   Fri July 20 21:06:15 2018 +0800

    append ABC

commit eaadf4e385e865d25c48e7ca9c8395c3f7dfaef0
Author: hxk <hxk@gmail.com>
Date:   Fri July 20 20:59:18 2018 +0800

    a new file
git log显示最近到最远的提交日志，我们可以看到两次提交，最后一次是append ABC

git的版本号是用SHA1计算出来的一个16进制数

如果嫌输出信息太多，可以加上--pretty=oneline

$ git log --pretty=oneline
1094adb7b9b3807259d8cb349e7df1d4d6477073 (HEAD -> master) append ABC
eaadf4e385e865d25c48e7ca9c8395c3f7dfaef0 a new file

### 4.5回退历史版本

$ git reset
首先，Git必须知道当前版本是哪个版本，在Git中，用HEAD表示当前版本，也就是最新的提交1094adb...，上一个版本就是HEAD^，上上一个版本就是HEAD^^，当然往上100个版本写100个^比较容易数不过来，所以写成HEAD~100。

回退上一版本

$ git reset --hard HEAD^
HEAD is now at eaadf4e a new file
 这时再次查看历史版本

$ git log
commit eaadf4e385e865d25c48e7ca9c8395c3f7dfaef0
Author: hxk <hxk@gmail.com>
Date:   Fri July 20 20:59:18 2018 +0800

    a new file
之前那个版本已经看不到了，这时如果想回到之前那个版本，需要知道版本号，git内部有个指向当前版本的head指针，将指针从当前版本指回去，所以git回退版本特别快

$ git reset --hard 1094adb7

### 4.6查看历史命令

要是不记得刚才的版本号了，可以使用以下命令：

$ git reflog

### 4.7查看状态

$ git status

## 5 工作区和暂存区

Git和SVN的一个不同之处就是有暂存区的概念

名词解释：

工作区（Working Directory）：指的是在电脑里能看到的目录，比如mymenu文件夹就是一个工作区

版本库（Repository）：.git目录，Git的版本库里存了很多东西，其中最重要的就是称为stage（或者叫index）的暂存区，还有Git为我们自动创建的第一个分支master，以及指向master的一个指针叫HEAD。

## 6修改

### 6.1管理修改

那么，为什么说git比svn优秀呢？因为git跟踪并管理的是修改，而不是文件

修改test.txt文件内容，添加一行

$ cat test.txt
Hello World ABC
This is the second line
然后添加文件

$ git add test.txt
再次修改test.txt

$ cat test.txt
Hello World ABC
This is the second line
This is the third line
提交

$ git commit -m "test add lines"
这时我们发现，第二次的修改未提交，这是为什么呢？

第一次修改-->git add-->第二次修改-->git commit

add将工作区的修改存入暂存区，但是第二次修改并未存入暂存区，git commit只负责把暂存区的修改提交，所以正确的顺序应该是：

第一次修改 --> git add --> 第二次修改 --> git add --> git commit

提交后，查看工作区和版本库里面最新版本的区别：

$ git diff HEAD -- test.txt

### 6.2撤销修改

1）丢弃工作区的修改 git checkout -- file（--很重要，没有--，就变成了“切换到另一个分支”的命令）：

$ git checkout -- test.txt
命令git checkout -- test.txt意思就是，把test.txt文件在工作区的修改全部撤销，这里有两种情况：

一种是test.txt自修改后还没有被放到暂存区，现在，撤销修改就回到和版本库一模一样的状态；

一种是test.txt已经添加到暂存区后，又作了修改，现在，撤销修改就回到添加到暂存区后的状态。

总之，就是让这个文件回到最近一次git commit或git add时的状态。

2）把暂存区的修改撤销掉（unstage），重新放回工作区  git reset HEAD <file>：

$ git reset HEAD test.txt
Unstaged changes after reset:
M    test.txt
git reset命令既可以回退版本，也可以把暂存区的修改回退到工作区。当我们用HEAD时，表示最新的版本。

### 6.3删除文件

工作区中删除文件

$ rm test.txt
一是要从版本库中删除该文件，那就用命令git rm删掉，并且git commit：

$ git rm test.txt
$ git commit -m "remove test.txt"
二是删错了，因为版本库里还有呢，所以可以很轻松地把误删的文件恢复到最新版本：

$ git checkout -- test.txt
git checkout其实是用版本库里的版本替换工作区的版本，无论工作区是修改还是删除，都可以“一键还原”。

PS: 手动删除文件，然后使用git rm <file>和git add<file>效果是一样的。
