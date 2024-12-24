import sys

# DP: 시간 초과 남
# def solution(n):
#     dp = [0 for _ in range(n+1)]
#     dp[1] = 1
#     for i in range(2, n+1):
#         root = int(i ** 0.5)
#         if root == i ** 0.5:
#             dp[i] = 1
#         else:
#             dp[i] = min([dp[i-j**2] for j in range(1, root+1)]) + 1
            
#     return dp[n]

# Brute force
def solution(n):
    root = int(n ** 0.5)
    if root == n ** 0.5:
        return 1
    
    squares = [i**2 for i in range(1, root+1)]
    squares_sum = []
    for i in range(len(squares)):
        for j in range(i, len(squares)):
            squares_sum.append(squares[i] + squares[j])
    
    if n in squares_sum:
        return 2
    else:
        for square in squares:
            if n - square in squares_sum:
                return 3
    return 4

n = int(sys.stdin.readline())
print(solution(n))