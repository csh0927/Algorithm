def solution(arr, divisor):
    answer = []
    cnt = 0
    for i in range(0, len(arr), 1):
        if arr[i] % divisor == 0:
            answer.append(arr[i])
            answer = sorted(answer)
            cnt += 1
            
    if cnt == 0:
        return [-1]
    
    return answer