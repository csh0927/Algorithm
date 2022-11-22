numlist = []

for i in range(0, 10, 1):
    n = int(input())
    numlist.append(n % 42)

numlist = set(numlist)
print(len(numlist))