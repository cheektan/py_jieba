# -*-coding:utf-8-*-
import codecs
path=r"C:\Users\12158\Downloads\py_jieba\批量处理\待处理"
respath=r"C:\Users\12158\Downloads\py_jieba\批量处理\已处理"
num=1
while num<=10:
    name="%d"%num
    filename=path+'\\'+str(name)+".txt"
    resname=respath+'\\'+str(name)+".txt"
    # file=codecs.open(filename,'r',encoding="utf-8").read()
    file=codecs.open(filename,'r',encoding='gbk')
    f=file.read()
    print(f)
    resfile=open(resname,'w',encoding='utf-8')
    resfile.write(f)
    num+=1

