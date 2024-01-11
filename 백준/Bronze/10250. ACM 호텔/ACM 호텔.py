c = int(input())

for i in range(c):
    h, w, n = map(int, input().split( ))

    f = n % h
    rc = n // h + 1

    if(f == 0):
        f = h
        rc -= 1
    
    result = f * 100 + rc
    print(result)