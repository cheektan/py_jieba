#-UTF-8
path=open('line.txt','r',encoding="UTF-8")
line=path.readline()
line=path.rstrip('\n')
print(line)
