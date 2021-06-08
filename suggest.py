import jieba
jieba.suggest_freq(('中','将'),True)
print('/'.join(jieba.cut('如果放到post中将出错。')))
