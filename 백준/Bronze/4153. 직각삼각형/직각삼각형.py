while True:
    numList = list(map(int, input().split()))
    if numList[0] == 0 and numList[1] == 0 and numList[2] == 0:
        break
    numList.sort()
    if numList[2]**2 == numList[0]**2 + numList[1]**2:
        print('right')
    else:
        print('wrong')