import jieba

fR=open('txt.txt', 'r', encoding='UTF-8')

sent=fR.read()
sent_list=jieba.lcut(sent)
print(" ".join(sent_list))

fW=open('txt_out.txt', 'w', encoding='UTF-8')
fW.write(' '.join(sent_list))
fW.write(' '.join(sent_list))

fR.close()
fW.close()