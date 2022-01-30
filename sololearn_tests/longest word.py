#skrypt znajduje najdłuższe słowo w tekście
txt = input()
num=[]
words=txt.split(' ')
#print(max(words))

for x in range(len(words)):
    num.append(len(words[x]))
najw=(max(num))
for y in range(len(words)):
    if len(words[y])==najw:
        print(words[y])
#your code goes here