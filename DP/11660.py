N, M = list(map(int, input().strip().split()))
table = []
dp = [[0 for _ in range(N+1)] for _ in range(N+1)]
for _ in range(N):
    table.append(list(map(int, input().strip().split())))

# 행 누적합
for i in range(N):
    s = 0
    for j in range(N):
        s += table[i][j]
        dp[i+1][j+1] = s

# dp[i][j] : (1,1) ~ (i,j)까지의 누적합
for i in range(1, N+1):
    for j in range(1, N):
        dp[j+1][i] += dp[j][i]

result = []
for _ in range(M):
    x1, y1, x2, y2 = list(map(int, input().strip().split()))
    sub_sum = dp[x2][y2] - dp[x2][y1-1] - dp[x1-1][y2] + dp[x1-1][y1-1]
    
    result.append(sub_sum)

for i in result:
    print(i)