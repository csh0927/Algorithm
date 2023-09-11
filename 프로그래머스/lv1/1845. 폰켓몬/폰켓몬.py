def solution(nums):
    mon_kind = len(set(nums))
    mon_choose_cnt = len(nums)//2
    answer = min(mon_kind, mon_choose_cnt)
    return answer