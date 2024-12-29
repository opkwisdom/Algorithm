import sys
from collections import deque

N = int(sys.stdin.readline())
G = []
for _ in range(N):
    G.append(list(map(int, sys.stdin.readline().split())))

P = [['0' for _ in range(N)] for _ in range(N)]

q = deque()
for s in range(1, N+1):
    q.append(s)
    while q:
        for _ in range(len(q)):
            u = q.popleft()
            for v in range(N):
                if P[s-1][v-1] == '0' and G[u-1][v-1] == 1:
                    P[s-1][v-1] = '1'
                    q.append(v)

for row in P:
    print(' '.join(row))