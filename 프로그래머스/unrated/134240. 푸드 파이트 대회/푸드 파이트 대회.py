def solution(food):
    answers = ""
    for i in range(1, len(food)):
        answers += str(i) * (food[i]//2)
    result = ''.join(reversed(answers))
    return answers + "0" + result