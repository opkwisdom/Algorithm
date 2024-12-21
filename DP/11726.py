def tiling(n):
    if n == 1:
        return 1
    W = [0] * n
    W[0] = 1
    W[1] = 2
    for i in range(2, n):
        W[i] = W[i-1] + W[i-2]
    return W[n-1]

n = int(input())
res = str(tiling(n))
print(res)
print(len(res))