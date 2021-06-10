# encoding=utf-8
import codecs
import os
import shutil
import jieba
import jieba.analyse
# jieba.enable_paddle()
jieba.load_userdict("dict.txt")  # 导入自定义词典
jieba.add_word('热运动') #添加关键词汇
def read_file_cut():  # Read file and cut
    path = r"C:\Users\12158\Downloads\py_jieba\批量处理\小说"  # create path
    # respath = r"C:\users\12158\Downloads\py_jieba\批量处理\小说"
    file = open('hit_stopwords.txt','r',encoding='UTF-8') #导入停用词
    stoplist = file.read().split()
    file.close()
    stopwords = {}.fromkeys(stoplist) #生成停用词词典
    # if os.path.isdir(respath): #清除respath文件夹
        # shutil.rmtree(respath, True)
    # os.makedirs(respath)
    num = 1
    while num <= 1: #遍历文档
        name = "%d" % num
        fileName = path + os.sep + str(name) + ".txt"
        resName = path + os.sep + 'res' + str(name) + ".txt"
        source = open(fileName, 'r', encoding='UTF-8')
        # if os.path.exists(resName): #清除resName文件
            # os.remove(resName)
        result = codecs.open(resName, 'w', encoding='UTF-8')
        line = source.readline()
        line = line.rstrip('\n')
        while line != "": #遍历文档单行
            # line = str(line,encoding="UTF-8")
            if line == '\n':
                line = ''
            final = ''
            seglist = jieba.lcut(line, use_paddle=True)
            for seg in seglist:
                if seg not in stopwords: #剔除单行停用词
                    final += seg
                seglist = jieba.lcut(final)
            output = ' '.join(seglist)
            # print(output)
            result.write(output + '\r\n')
            # output = output.rsplit('\n')
            # result.write(output)
            line = source.readline()
            # line = line.rstrip('\n')
        else:
            # print('End file:' + str(num))
            source.close()
            result.close()
        num += 1
    else:
        print('End All')
if __name__ == '__main__':  # Run function
    read_file_cut()
