import sys
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

N, M = list(map(int, sys.stdin.readline().split()))
maze = []
for _ in range(N):
    maze.append(sys.stdin.readline().strip())
dist = [[0 for _ in range(M)] for _ in range(N)]
dist[0][0] = 1

q = deque()
q.append((0,0))

while q:
    for _ in range(len(q)):
        y, x = q.popleft()
        d = dist[y][x]
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if ny < 0 or ny >= N or nx < 0 or nx >= M:
                continue
            if not dist[ny][nx] and maze[ny][nx] == '1':
                dist[ny][nx] = d + 1
                q.append((ny,nx))

print(dist[N-1][M-1])