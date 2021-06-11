from gensim import corpora, models
words_ls=[]
review_list=[]
txt_id=1
f=open('txt.txt','r',encoding='utf-8').readline()
for line in f:
    review_words=line.split()
    # print(review_words)
    words_ls.append(review_words)
print(words_ls)
dictionary=corpora.Dictionary(words_ls)
corpus=[dictionary.doc2bow(words) for words in words_ls]
print(corpus)
lda=models.ldamodel.LdaModel(corpus=corpus,id2word=dictionary,num_topics=5)
for topic in lda.print_topics(num_words=3):
    print(topic)
