def maximize_scores():
    dp = [[0 for _ in range(N+1)] for i in range(2)]
    dp[0][1], dp[1][1] = stickers[0][0], stickers[1][0]
    if N == 1:
        return max(dp[0][1], dp[1][1])
    
    dp[0][2] = stickers[1][0] + stickers[0][1]
    dp[1][2] = stickers[0][0] + stickers[1][1]
    if N == 2:
        return max(dp[0][2], dp[1][2])
    
    for i in range(3, N+1):
        dp[0][i] = max(dp[1][i-2], dp[1][i-1]) + stickers[0][i-1]
        dp[1][i] = max(dp[0][i-2], dp[0][i-1]) + stickers[1][i-1]

    return max(dp[0][N], dp[1][N])

T = int(input())
result = []
for _ in range(T):
    N = int(input())
    stickers = []
    for _ in range(2):
        stickers.append(list(map(int, input().strip().split())))
    max_val = maximize_scores()
    result.append(max_val)

for res in result:
    print(res)