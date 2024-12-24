import sys

def tiling2(n):
    if n == 1:
        return 1
    
    dp = [0 for _ in range(n+1)]
    dp[1], dp[2] = 1, 3
    for i in range(3, n+1):
        dp[i] = dp[i-1] + 2 * dp[i-2]
    return dp[n] % 10007

n = int(sys.stdin.readline())

print(tiling2(n))