n1 = int(input())
n2 = int(input())
n3 = int(input())

gop = list(str(n1 * n2 * n3))

for i in range(10):
    print(gop.count(str(i)))