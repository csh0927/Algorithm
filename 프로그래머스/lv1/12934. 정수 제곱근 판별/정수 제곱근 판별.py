def solution(n):
    answer = 0
    answer = n**(1/2)   
    if int(answer)**2 == n:
        return (answer+1)**2
    else :
        return -1
    return answer