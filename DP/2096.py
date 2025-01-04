N = int(input())
max_dp = [[0, 0, 0],
          [0, 0, 0]]
min_dp = [[0, 0, 0],
          [0, 0, 0]]

for _ in range(N):
    table = list(map(int, input().strip().split()))

    for j in range(3):
        if j == 0:
            max_dp[1][j] = max(max_dp[0][0], max_dp[0][1]) + table[0]
            min_dp[1][j] = min(min_dp[0][0], min_dp[0][1]) + table[0]
        elif j == 1:
            max_dp[1][j] = max(max_dp[0][0], max_dp[0][1], max_dp[0][2]) + table[1]
            min_dp[1][j] = min(min_dp[0][0], min_dp[0][1], min_dp[0][2]) + table[1]
        else:
            max_dp[1][j] = max(max_dp[0][1], max_dp[0][2]) + table[2]
            min_dp[1][j] = min(min_dp[0][1], min_dp[0][2]) + table[2]
    max_dp[0] = max_dp[1][:]
    min_dp[0] = min_dp[1][:]

if N == 1:
    print(max(table), min(table))
else:
    print(max(max_dp[1]), min(min_dp[1]))