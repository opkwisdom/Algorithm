A = input().strip()
B = input().strip()

M, N = len(A), len(B)
table = [[0 for _ in range(N+1)] for _ in range(M+1)]
i, j = 0, 0

for i in range(1, M+1):
    for j in range(1, N+1):
        if A[i-1] == B[j-1]:
            table[i][j] = table[i-1][j-1] + 1
        else:
            table[i][j] = max(table[i-1][j], table[i][j-1])

print(table[M][N])