a = int(input())
data = list(map(int, input().split()))
dp = [i for i in data]

for i in range(a) :
	for j in range(i) :
		if data[j] < data[i] :
			dp[i] = max(dp[i], dp[j] + data[i])

print(max(dp))