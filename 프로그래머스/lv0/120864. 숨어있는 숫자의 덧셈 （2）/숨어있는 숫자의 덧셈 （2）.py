import re
def solution(my_string):
    #데이터 매개변수 확인
    #숫자 판단
        #문자가 대소문자, 자연수인지 확인
    #연속된 수는 하나의 수로 간주
    answer = re.findall(r'\d+', my_string)
    return sum(list(map(int, answer)))