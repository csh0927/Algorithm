k, n = map(int, input().split())
a=[int(input()) for i in range(k)]
start = 1
end = max(a)

while start <= end:
    mid = (start + end) // 2
    cnt = 0

    for i in a:
        cnt += i//mid
    
    if cnt < n:
        end = mid-1

    else :
        start = mid+1

print(end)