def solution(p, s):
    answer = []
    t = 0
    cnt = 0
    
    while len(p) > 0:
        if (p[0] + t*s[0]) >= 100: #가장 앞에 있는 수가 100 이상이 될 때까지 반복한다.
            p.pop(0) 
            s.pop(0)
            cnt += 1 #100 이상이 되면 p와 s에서 가장 앞에 있는 수를 pop하고 cnt를 하나 늘린다.
            
        else: 
            if cnt > 0: #100이 안 되고 cnt가 0보다 크다면 cnt를 answer에 추가하고 cnt를 초기화
                answer.append(cnt)
                cnt = 0
            t += 1
            
    answer.append(cnt) #반복이 끝난 후, cnt를 answer에 추가한다
    
    return answer