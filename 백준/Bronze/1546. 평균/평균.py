n = int(input())
numList = list(map(int, input().split()))
maxN = max(numList)
newList = []

for i in numList:
    newList.append(i/maxN * 100)
avg = sum(newList)/n
print(avg)