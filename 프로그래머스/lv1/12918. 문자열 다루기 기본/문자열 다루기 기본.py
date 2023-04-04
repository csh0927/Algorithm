def solution(s):
    if len(s) != 4 and len(s) != 6:
        return False
    ls = list(s)
    for i in ls:
        if i.isalpha():
            return False
    return True