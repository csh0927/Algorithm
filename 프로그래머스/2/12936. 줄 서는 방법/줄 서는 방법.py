import math
 
def solution(n, k):
    nl = [i for i in range(1, n + 1)]
    answer = []
    
    while nl:
        i = (k - 1) // math.factorial(n - 1)
        answer.append(nl.pop(i))
 
        k = k % math.factorial(n - 1)
        n -= 1
 
    return answer