import math

def solution(b, y):
    answer = []
    c = (b // 2) + 2 #전체 타일의 가로와 세로의 합이다.
    w = math.ceil(c / 2)
    
    while c > w: #가로 길이가 세로 길이보다 클 때까지 반복한다.
        h = c - w
        check = (w-2) * (h-2) #내부 타일 수 계산
        
        if check == y: #check가 y와 일치할 경우 answer에 가로, 세로를 저장한다.
            answer = [w, h]
            break
        
        w += 1
    
    return answer