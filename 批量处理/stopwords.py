import jieba
file = open('批量处理/hit_stopwords.txt', 'r', encoding='UTF-8').read().split()
# stopwords = dict.fromkeys(['，','。','：','；','\n'])
stopwords = {}.fromkeys(file)
text = open('TXT/txt.txt', 'r', encoding='UTF-8').read()
segs = jieba.lcut(text)
final = ''
for seg in segs:
    if seg not in stopwords:
        final += seg
final = jieba.lcut(final)
line = ' '.join(final)
print(line)
