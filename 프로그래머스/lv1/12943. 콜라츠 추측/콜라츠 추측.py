def solution(num):
    if num == 1:
        return 0
    answer = 0
    while(True):
        if num % 2 == 0:
            num = num//2
            answer += 1
        elif num % 2 != 0:
            num *= 3
            num += 1
            answer += 1
        if answer >= 500:
            return -1
        if num == 1:
            break
    return answer