word = input().upper()
wordList = list(set(word))

cnt = []
for i in range(len(wordList)):
    cnt.append(word.count(wordList[i]))
Max = max(cnt)
if cnt.count(Max) != 1:
    print('?')
else :
    print(wordList[cnt.index(Max)])