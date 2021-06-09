#encoding=utf-8
import sys
import re
import codecs
import os
import shutil
import jieba
import jieba.analyse
#jieba.enable_paddle()
jieba.load_userdict("dict.txt") #导入自定义词典
def read_file_cut(): #Read file and cut
        fileName ="line.txt"
        resName = "outline.txt"
        source = open(fileName,'r',encoding='UTF-8')
        result = open(resName,'w',encoding='UTF-8')
        line = source.readline()
        print(line)
        line = source.readline()
        print(line)
        line = line.rstrip('\n')
        print(line)
        while line!="":
            #print(line)
            seglist = jieba.lcut(line,use_paddle=True)
            output = ' '.join(seglist)
            #print(output)
            result.write(output + '\n')
            line = source.readline()
            #print(line)
        source.close()
        result.close()
if __name__ == '__main__': #Run function
    read_file_cut()