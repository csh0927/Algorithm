def solution(s):
    result = []
    ls = sorted([s.split(',') for s in s[2:-2].split('},{')], key = len)
    for l in ls:
        for s in l:
            if int(s) not in result:
                result.append(int(s))
                break
    return result