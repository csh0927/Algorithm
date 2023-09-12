from collections import Counter

def solution(participant, completion):
    answer = ''
    
    p_dic = Counter(participant)
    c_dic = Counter(completion)
    
    for p_name in p_dic:
        if p_dic[p_name] != c_dic[p_name]:
            answer = p_name
    
    return answer