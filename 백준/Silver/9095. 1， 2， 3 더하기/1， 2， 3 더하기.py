n = int(input())
nl = []

def f(n):
    if n == 1: return 1

    if n == 2: return 2

    if n == 3: return 4

    return f(n-1) + f(n-2) + f(n-3)


for i in range(0, n):
    e = int(input())
    nl.append(e)

for i in range(0, n):
    print(f(nl[i]))