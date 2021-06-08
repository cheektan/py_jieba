#encoding=utf-8
import sys
import re
import codecs
import os
import shutil
import jieba
import jieba.analyse

jieba.load_userdict("dict.txt") #导入自定义词典
def read_file_cut(): #Read file and cut
    path = r"C:\Users\12158\Downloads\py_jieba\批量处理\待处理" #create path
    respath = r"C:\users\12158\Downloads\py_jieba\批量处理\已处理"
    if os.path.isdir(respath):
        shutil.rmtree(respath,True)
    os.makedirs(respath)
    num = 1
    while num<=10:
        name = "%d" % num
        fileName = path + os.sep + str(name) + ".txt"
        resName = respath + os.sep + str(name) + ".txt"
        source = open(fileName,'r',encoding='UTF-8')
        if os.path.exists(resName):
            os.remove(resName)
        result = codecs.open(resName,'w',encoding='UTF-8')
        line = source.readline()
        line = line.rstrip('\n')
        while line!="":
            #line = str(line,"utf-8")
            seglist = jieba.cut(line,cut_all=False)
            output = ' '.join(list(seglist))
            print(output)
            result.write(output + '\r\n')
            line = source.readline()
        else:
            print('End file:' + str(num))
            source.close()
            result.close()
        num = num + 1
    else:
        print('End All')
if __name__ == '__main__': #Run function
    read_file_cut()