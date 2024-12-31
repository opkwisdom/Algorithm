import sys
from collections import deque

N = int(sys.stdin.readline())
P = [0 for _ in range(N+1)]
P[1] = 1    # Root
G = {}

for _ in range(N-1):
    a, b = list(map(int, sys.stdin.readline().split()))
    G[a] = G.get(a, [])
    G[a].append(b)
    G[b] = G.get(b, [])
    G[b].append(a)

q = deque([1])
while q:
    for _ in range(len(q)):
        u = q.popleft()
        for v in G[u]:
            if not P[v]:
                P[v] = u
                q.append(v)

for i in range(2, N+1):
    print(P[i])
