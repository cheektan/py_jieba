from jieba import Tokenizer, analyse
textrank=analyse.textrank
analyse.set_idf_path('idf.txt.big')
analyse.set_stop_words('hit_stopwords.txt')
text=open('res1.txt','r',encoding='utf-8').read()
print('keywords by textrank:')
keywords=textrank(text,topK=5)
f=open('z3.txt','w',encoding='utf-8')
for keyword in keywords:
    # print(keyword)
    f.write(keyword+'/')
f.close()
