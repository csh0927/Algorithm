n = int(input())
nn = n - 1
b = 1
for i in range(1, n + 1, 1):
    for j in range(nn, 0, -1):
        print(" ", end='')
    for j in range(1, b + 1, 1):
        print("*", end='')
    b += 2
    nn -= 1
    print()
n -= 1
outp = n*2 - 1
for i in range(1, n + 1, 1):
    for j in range(1, i + 1, 1):
        print(" ", end='')
    for j in range(1, outp + 1, 1):
        print("*", end='')
    outp -= 2
    print()