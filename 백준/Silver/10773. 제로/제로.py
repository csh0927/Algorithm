n = int(input())
nl = []
for i in range(n):
    a = int(input())
    if a == 0:
        nl.pop(-1)
        continue
    nl.append(a)

print(sum(nl))