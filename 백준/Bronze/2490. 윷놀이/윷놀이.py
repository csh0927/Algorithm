for i in range(1, 4, 1):
    nol = list(map(int, input().split()))
    cnt = 0
    for j in range(0, 4, 1):
        if nol[j] == 0:
            cnt += 1
    if cnt == 1:
        print("A")
    elif cnt == 2:
        print("B")
    elif cnt == 3:
        print("C")
    elif cnt == 4:
        print("D")
    else : print("E")