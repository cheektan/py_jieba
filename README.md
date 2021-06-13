# **jieba分词练习**  
## 1. 分词  
* 文本分词
* txt文档分词

## 2. 分词文件保存
- 创建新文档保存分词结果
- excludes.txt, 排除one word, 
- 文档批量分词，批量保存-multi_stopwords_txt
## 3. 分词词频统计
* 对分词结果进行频率排序，并统计词频，导入excel
* 关键词提取 `TF-IDF` `TextRank`
## Working for 
- ~~multi_stopwords_txt~~
- ~~去除txt中空行~~
- ~~txt文档编码格式转成UTF-8~~
- ~~analyse使用-关键词、停用词~~
- 同义词组合并替换
- 词频可视化-词图
- ~~可导入excel~~  

[](这是Markdown注释代码&超链接) 

### $其他实现功能:  
- 批量更改文件名扩展名
- 多文档合并
- 多文档编码格式转换:`"ANIS"--"UTF-8"` notepad++ & Editplus

-----------
## Mark:
- Note:  
  - `print(str,seg='*',end='\n')` _默认换行_
  - `newF.write(str)` _默认不换行_
  - `str=flie.readline()` _单行读取带 '\n'_ 