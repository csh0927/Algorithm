go, byun, su = map(int, input().split())

if byun >= su :
    print(-1)
else : print(go//(su - byun) + 1)