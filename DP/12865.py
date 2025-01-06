N, K = map(int, input().split())
items = []
for _ in range(N):
    w, v = map(int, input().split())
    items.append((w, v))

items = sorted(items, key=lambda item: item[0])
X = [[0 for _ in range(K+1)] for _ in range(N+1)]

for i in range(1, N+1):
    total_w = sum([w for w, v in items[:i]])
    max_range = min(total_w, K)
    # DP Idea
    for j in range(1, max_range+1):
        if j - items[i-1][0] >= 0:
            X[i][j] = max(X[i-1][j], X[i-1][j-items[i-1][0]] + items[i-1][1])
        else:
            X[i][j] = X[i-1][j]
    # Optimization
    for j in range(max_range+1, K+1):
        X[i][j] = X[i][j-1]

print(X[N][K])