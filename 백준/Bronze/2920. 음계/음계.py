nl = list(map(int, input().split()))

if nl == sorted(nl):
    print("ascending")
elif nl == sorted(nl, reverse=True):
    print("descending")
else : print("mixed")