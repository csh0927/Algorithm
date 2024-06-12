def solution(s, k):
    l, r = 0, 0
    ans = [0, len(s)]
    sum = s[0]

    while True:
        if sum < k:
            r += 1
            if r == len(s):
                break
            sum += s[r]
            
        else:
            if sum == k:
                if r-l < ans[1] - ans[0]:
                    ans = [l, r]
            sum -= s[l]
            l += 1
    return ans