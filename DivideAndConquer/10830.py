

def mul(U, V):
    n = len(U)
    Z = [[0]*n for _ in range(n)]

    for row in range(n):
        for col in range(n):
            e = 0
            for i in range(n):
                e += U[row][i] * V[i][col]
            Z[row][col] = e % 1000
    return Z

def power(A, B):
    if B == 1:
        for row in range(len(A)):
            for col in range(len(A)):
                A[row][col] %= 1000
        return A
    
    tmp = power(A, B//2)
    if B % 2:
        return mul(mul(tmp, tmp), A)
    else:
        return mul(tmp, tmp)


N, B = map(int, input().split())
A = []
for _ in range(N):
    A.append(list(map(int, input().split())))

matrix = power(A, B)
for i in range(len(matrix)):
    print(*matrix[i])