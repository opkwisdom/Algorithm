import sys
from collections import deque

N, M = list(map(int, sys.stdin.readline().split()))
net = {}
for _ in range(M):
    u, v = list(map(int, sys.stdin.readline().split()))
    net[u] = net.get(u, [])
    net[u].append(v)
    net[v] = net.get(v, [])
    net[v].append(u)
visited = [[False for _ in range(N)] for _ in range(N)]
for i in range(N):
    visited[i][i] = True

APSP = [[0 for _ in range(N)] for _ in range(N)]

for s in range(1, N+1):
    dist = 1
    q = deque()
    q.append(s)
    while q:
        for _ in range(len(q)):
            u = q.popleft()
            for v in net[u]:
                if not visited[s-1][v-1]:
                    visited[s-1][v-1] = True
                    APSP[s-1][v-1] = dist
                    q.append(v)
        dist += 1

kevin_bacons = []
for row in APSP:
    kevin_bacons.append(sum(row))

current_min = 1000000
min_ = -1
for idx in range(len(kevin_bacons)):
    if kevin_bacons[idx] < current_min:
        min_ = idx + 1
        current_min = kevin_bacons[idx]
print(min_)