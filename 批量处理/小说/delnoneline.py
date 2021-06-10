# -*- coding: UTF-8 -*-
txt = open(r'C:\Users\12158\Downloads\py_jieba\批量处理\小说\2.txt','r',encoding='UTF-8')
line = txt.readline()
print(line)
file = open(r'C:\Users\12158\Downloads\py_jieba\批量处理\小说\3.txt','w',encoding='UTF-8')
while line != '':
    # line = line.strip('\n')
    if line == '\n':
        line = ''
    print(line)
    file.write(line)
    line = txt.readline()
# else:
    # line = txt.readline()
txt.close()
file.close()
