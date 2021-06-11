# -*- coding: utf-8 -*-
# from jieba import analyse
import jieba.analyse
tfidf=jieba.analyse.extract_tags
jieba.analyse.set_idf_path('idf.txt.big') #自定义语料
jieba.analyse.set_stop_words('hit_stopwords.txt') #加载停用词
text=open('res1.txt','r',encoding='utf-8').read()
keywords=tfidf(text,topK=5)
# print('keywords by tfidf:')
f=open('z.txt','w',encoding='utf-8')
for keyword in keywords:
    # print(keyword,'')
    f.write(keyword+'/')
f.close()