n = int(input())
numList = list(map(int, input().split()))
maxN = max(numList)
evenList = []

for i in numList:
    evenList.append(i/maxN * 100)
even = sum(evenList)/n
print(even)