f=open('excludes.txt','r',encoding='UTF-8')
excludes=f.read().split()
f.close()
print(excludes)