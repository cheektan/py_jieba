import jieba

jieba.enable_paddle()
strs=["我来到北京大学","乒乓球拍卖完了","中国科技大学"]
for str in strs:
    seg_list = jieba.cut(str,use_paddle=True)
    print("Paddle Mode: " +'/'.join(list(seg_list)))

seg_list = jieba.cut("我来到北京清华大学", cut_all=True)
print("Full Mode: " + "/".join(seg_list))

seg_list = jieba.cut("我来到北京清华大学", cut_all=False)
print("Default Mode: " + "/".join(seg_list))

seg_list = jieba.cut("他来到网易杭研大厦")
print("/".join(seg_list))

seg_list = jieba.cut_for_search("小明硕士毕业于中国科学院计算所，后在日本京都大学深造")
print("/".join(seg_list))