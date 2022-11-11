n = int(input())
b = n*2 - 1
for i in range(1, n + 1, 1):
    for j in range(1, i, 1):
        print(" ", end='')
    for j in range(1, b + 1, 1):
        print("*", end='')
    b -= 2
    print()