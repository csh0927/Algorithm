def solution(n):
    answer = ''
    answer = "수박"*(n//2)
    if n % 2 != 0:
        answer = list(answer)
        answer.append("수")
        return ''.join(answer)
    return answer