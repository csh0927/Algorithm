def solution(numbers):
    answer = 0
    ist = []
    for i in range(0, len(numbers)):
        for j in range(i + 1, len(numbers)):
            ist.append(numbers[i] * numbers[j])
    return max(ist)