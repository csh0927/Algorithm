n = int(input())

outp = n*2 - 1
for i in range(1, n + 1, 1):
    for j in range(1, i, 1):
        print(" ", end='')
    for j in range(1, outp + 1, 1):
        print("*", end='')
    outp -= 2
    print()
nn = n - 1
b = 1
for i in range(1, n, 1):
    for j in range(nn, 1, -1):
        print(" ", end='')
    for j in range(1, b + 3, 1):
        print("*", end='')
    b += 2
    nn -= 1
    print()