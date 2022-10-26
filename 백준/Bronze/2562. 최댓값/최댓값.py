b = 0
num = []
for i in range(0, 9, 1):
    num.append(int(input()))
    if num[i] > b:
        b = num[i]
print(b)
print(num.index(b) + 1)