mod = 1000000009

d = [[0,0,0] for _ in range(100000)]
d[0] = [1,0,0]
d[1] = [0,1,0]
d[2] = [1,1,1]

for i in range(3,100000):
  d[i][0] = (d[i-1][1] % mod + d[i-1][2] % mod) % mod
  d[i][1] = (d[i-2][0] % mod + d[i-2][2] % mod) % mod
  d[i][2] = (d[i-3][0] % mod + d[i-3][1] % mod) % mod

for _ in range(int(input())):
  n = int(input())
  print((d[n-1][0]+d[n-1][1]+d[n-1][2]) % mod)
