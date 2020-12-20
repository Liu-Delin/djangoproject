## 这是一个Django代码示例
### 安装Django
1. 如果是用pip来安装，需要提前安装好python3。可以参照[官方安装指南](https://docs.djangoproject.com/en/3.1/intro/install/)。
2. 如果是用安装包来安装，它会自带有python3。可以去[下载安装包](https://bitnami.com/stack/django/installer)
3. 安装完成后验证：`python -m django --version`，会出现这样的结果：`3.1.4`。
### 运行代码
1. 把本项目代码下载到本地。
2. 创建文件数据库（sqlite3）。
    
    cd到项目路径，运行命令`python manage.py migrate`来创建数据库。会出现如下结果，也会创建一个`db.sqlite3`的数据库文件。
```
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, projects, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  ...
  Applying projects.0001_initial... OK
  Applying sessions.0001_initial... OK
```
3. 创建管理员账户。

    运行命令`python manage.py createsuperuser`来创建超级用户。
4. 启动项目。

    运行命令`python manage.py runserver`来启动项目。会出现如下结果：
 ```
December 20, 2020 - 05:44:40
Django version 3.1.4, using settings 'djangoproject.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
 ```
 5. 创建数据。
 
     进入[管理员页面](http://127.0.0.1:8000/admin)并输入刚刚创建的用户名密码。在管理员页面里能够进行数据的查看、修改、删除。

![image](https://user-images.githubusercontent.com/58288007/102707767-b7442e00-42d8-11eb-8200-5371b342107e.png)
     
 6. 访问数据。
 
     进入[所有项目页面](http://127.0.0.1:8000/projects/)查看所有项目。
 ![image](https://user-images.githubusercontent.com/58288007/102707819-35a0d000-42d9-11eb-84b3-2d69af85e451.png)
     点击其中的具体项目查看详细内容。
 ![image](https://user-images.githubusercontent.com/58288007/102707836-56692580-42d9-11eb-88f4-2fa68d202f50.png)
 
 ### 未完成部分
 1. 用户进行额度申请功能未实现。
 2. 用户查看自己提交的申请功能未实现。
 3. 用户上传附件功能未实现。
 4. 界面没有美化。
