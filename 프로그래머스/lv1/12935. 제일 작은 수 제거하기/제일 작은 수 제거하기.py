def solution(arr):
    n = 0
    if len(arr) == 1:
        arr[0] = -1
    else :
        arr.remove(min(arr))
    return arr