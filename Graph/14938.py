import sys

input = sys.stdin.readline
INF = float('inf')

n, m, r = map(int, input().split())
dist = [[INF for _ in range(n+1)] for _ in range(n+1)]
for i in range(n+1):
    dist[i][i] = 0

t = list(map(int, input().split()))

# Initialize
for _ in range(r):
    a, b, l = map(int, input().split())
    dist[a][b] = dist[b][a] = l

# Floyd-Washall (=O(N^3))
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

# Find max value
max_val = 0
for i in range(1, n+1):
    cur_val = 0
    for j in range(1, n+1):
        if dist[i][j] <= m:
            cur_val += t[j-1]
    max_val = max(max_val, cur_val)
    
print(max_val)