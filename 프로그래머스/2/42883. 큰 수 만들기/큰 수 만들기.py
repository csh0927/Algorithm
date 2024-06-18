def solution(num, k):
    answer = []
    
    for n in num:
        while answer and answer[-1] < n and k > 0:
            #answer의 마지막 수보다 n이 더 크고, 제거할 수 있는 횟수가 남아 있는 동안 반복한다.
            k -= 1
            answer.pop() #제거할 수 있는 횟수를 줄이고 더 작은 수를 pop한다.
        answer.append(n) 
    
    return ''.join(answer[:len(num) - k]) #필요한 길이만큼 잘라서 문자열로 반환한다.