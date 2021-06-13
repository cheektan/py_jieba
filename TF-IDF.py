# -*- coding: utf-8 -*-
# from jieba import analyse
import jieba.analyse
tfidf = jieba.analyse.extract_tags
jieba.analyse.set_idf_path('TXT\\idf.txt.big')  # 自定义语料
jieba.analyse.set_stop_words('TXT\\hit_stopwords.txt')  # 加载停用词
text = open('TXT\\txt.txt', 'r', encoding='utf-8').read()
keywords = tfidf(text, topK=5)
# print('keywords by tfidf:')
f = open('TXT\\z.txt', 'w', encoding='utf-8')
for keyword in keywords:
    # print(keyword,'')
    f.write(keyword+'/')
f.close()
