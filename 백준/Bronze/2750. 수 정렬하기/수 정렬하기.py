N = int(input())
numlist = []

for i in range(0, N, 1):
    n = int(input())
    numlist.append(n)

numlist.sort(reverse=True)

for i in range(N - 1, -1, -1):
    print(numlist[i])