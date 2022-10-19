n = int(input())

for i in range(n):
    N, W = input().split()

    for j in W:
        print(j * int(N), end='')
    print()