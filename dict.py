import jieba
jieba.enable_paddle()
jieba.load_userdict("dict.txt") #自定义词典
jieba.suggest_freq(('区','块'),True) #词频
jieba.add_word('君意')
#jieba.add_word('小小明')
print ("/".join(jieba.lcut("大连美容美发学校中君意是你值得信赖的选择")))
print("/".join(jieba.lcut('小胡想知道区块链是什么。',use_paddle=True)))