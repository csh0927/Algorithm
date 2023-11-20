a = int(input())
N = []

for i in range(a):
    b = int(input())
    N.append(b)

Dp = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9] + [0] * 91

for i in range(a):
    for j in range(11, N[i]+1):
        if N[i] < 11:
            break;
        
        Dp[j] = Dp[j-1] + Dp[j-5]

        
    print(Dp[N[i]])
