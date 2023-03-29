def solution(x):
    xL = list(map(int, str(x)))
    n = sum(xL)
    print(n)
    if x % n == 0:
        return True
    else: return False