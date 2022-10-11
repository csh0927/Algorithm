n1 = int(input())
numlist1 = set(map(int, input().split()))
n2 = int(input())
numlist2 = list(map(int, input().split()))

for num in numlist2:
    print(1) if num in numlist1 else print(0)
