def solution(phone_number):
    answer = ''
    n = len(phone_number)
    phone_number = list(phone_number)
    for i in range(0, n-4, 1):
        phone_number[i] = '*'
    
    for s in phone_number:
        answer += s + ""
        
    
    return answer.strip()