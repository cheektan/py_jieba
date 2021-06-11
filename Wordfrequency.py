from re import T
import jieba

import xlwt #写入Excel表的库
wbk=xlwt.Workbook(encoding='ascii')
sheet=wbk.add_sheet('wordcount')#Excel单元格名字

jieba.enable_paddle()
def takeSecond(elem):
    return elem[1]
def main():
    file=open("txt.txt","r",encoding="UTF-8")
    text=file.read()
    file.close()
    words=jieba.lcut(text)
    counts={}
    fW=open('Wordfrequency.txt','w',encoding='UTF-8') #创建保存文件
    for word in words:
        if len(word)==1: #排除长度为一的word
            continue
        else:
            counts[word]=counts.get(word,0) + 1
        file=open("excludes.txt","r",encoding='UTF-8')
        #excludes=['平均','始终','随机','进行','无规','统计','作用','过程','结果']
        excludes=file.read().split() #['str','str']
        file.close()
        for delword in excludes:
            try:
                del counts[delword]
            except:
                continue
    items=list(counts.items())
    items.sort(key=takeSecond,reverse=True)
    for i in range(10):
        item=items[i]
        keyWord=item[0]
        count=item[1]
        print("{0:<10}{1:>5}".format(keyWord,count))
        #print('%3s,%d'%(keyWord,count))
        fW.write('%s %d\n'%(keyWord,count)) #写入词组词频
    fW.close()
    for i in range(10): #保存成xls表格
        item=items[i]
        sheet.write(i,1,label=item[1])
        sheet.write(i,0,label=item[0])
    wbk.save('wordcount.xls')
main()