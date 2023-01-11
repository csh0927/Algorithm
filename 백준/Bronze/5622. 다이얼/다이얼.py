dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
a = input()
n = 0

for i in range(len(a)):
    for j in dial:
        if a[i] in j:
            n += dial.index(j) + 3

print(n)