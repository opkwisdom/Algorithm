import sys
input = sys.stdin.readline
INF = float('inf')

N = int(input())
M = int(input())

G = [[INF for _ in range(N)] for _ in range(N)]
for i in range(N):
    G[i][i] = 0

for _ in range(M):
    u, v, w = map(int, input().split())
    G[u-1][v-1] = min(G[u-1][v-1], w)

# Floyd-Washall
for k in range(N):
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            G[i][j] = min(G[i][j], G[i][k]+G[k][j])

# 못 가는 경우에는 0
for i in range(N):
    for j in range(N):
        if G[i][j] == INF:
            G[i][j] = 0

for row in G:
    print(*row)