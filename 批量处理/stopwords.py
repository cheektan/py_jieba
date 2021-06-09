import jieba
file = open('hit_stopwords.txt','r',encoding='UTF-8').read().split()
# stopwords = dict.fromkeys(['，','。','：','；','\n'])
stopwords = {}.fromkeys(file)
text = open('line.txt','r',encoding='UTF-8').read()
segs = jieba.lcut(text)
final = ''
for seg in segs:
    if seg not in stopwords:
        final += seg
final = jieba.lcut(final)
line = ' '.join(final)
print(line)

