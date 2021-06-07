import jieba

str=jieba.lcut("我在厦门大学物理科学与技术学院读硕士研究生")
print(" ".join(str))

fW=open('demo.txt','w',encoding='UTF-8')
fW.write(' '.join(str))
fW.close()