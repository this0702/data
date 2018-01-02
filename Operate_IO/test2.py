import os
# print(os.name)#操作系统类型
# print(os.environ)#环境变量
# print(os.environ['path'])#环境变量返回dict
# print(os.path.abspath('.'))#获得当前目录绝对路径


#创建删除一个目录
# os.path.join('E:\python_code\Operate_IO','testdir')#
# os.mkdir('E:/python_code/Operate_IO/testdir')
# os.rmdir('E:/python_code/Operate_IO/testdir')
#.join()函数，这样可以正确处理不同操作系统的路径分隔符
# os.path.join('E:\python_code\Operate_IO','testdir')#
#这样调用split就成了绝对路径和相对路径分开
# print(os.path.split('E:/python_code/Operate_IO/testdir'))#直接分为tuple


# #对文件进行操作
# os.rename()
# os.remove()
# import shutil#对os的补充，
# help(shutil.copy)


#对文件进行过滤
print([x for x in os.listdir('.') if os.path.isdir(x)])
print( [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'])


