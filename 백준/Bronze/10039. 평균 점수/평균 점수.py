hap = 0
nl = []
for i in range(5):
    n = int(input())
    nl.append(n)
for i in nl:
    if i < 40:
        i = 40
    hap += i

print(int(hap/5))