import os
#import pandas as pd
path=r'C:\Users\12158\Downloads\py_jieba\123'
files=os.listdir(path) #得到文件夹下的所有文件名称
txts=[]
for file in files: #遍历文件夹
    position=path + '\\' + file #构造绝对路径
    print(position)
    with open(position, 'r', encoding='UTF-8') as f: #打开文件
        data=f.read() #读取文件
        txts.append(data)
txts='，'.join(txts) #转化为非数组类型
print(txts)
fw=open('文本合并.txt','w',encoding='UTF-8')
fw.write(txts)
fw.close()