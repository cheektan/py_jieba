import os
path=r'C:\Users\12158\Downloads\py_jieba\123'
filelist=os.listdir(path) #获取该目录下所有文件，存入列表中
n=0
for i in filelist:
    oldname=path+os.sep+filelist[n] #设置旧文件名 os.sep添加系统分隔符
    newname=path+os.sep+'文本'+str(n+1)+'.txt' #设置新文件名
    os.rename(oldname,newname) #文件改名
    print(oldname,'======>',newname)
    n+=1