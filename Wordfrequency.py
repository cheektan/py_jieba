import jieba
def takeSecond(elem):
    return elem[1]
def main():
    path="doc.txt"
    file=open(path,"r",encoding="UTF-8")
    text=file.read()
    file.close()
    words=jieba.lcut(text)
    counts={}
    fW=open('two.txt','w',encoding='UTF-8')
    for word in words:
        counts[word]=counts.get(word,0) + 1
    items=list(counts.items())
    items.sort(key=takeSecond,reverse=True)
    for i in range(20):
        item=items[i]
        keyWord=item[0]
        count=item[1]
        print("{0:<10}{1:>5}".format(keyWord,count))
        fW.write("{0:<5}{1:>2}".format(keyWord,count,  ))
        fW.write("\n")
    fW.close()
main()