import sys
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

N, M = list(map(int, sys.stdin.readline().split()))
campus = []
for _ in range(N):
    campus.append(sys.stdin.readline().strip())
visited = [[False for _ in range(M)] for _ in range(N)]

for y in range(N):
    for x in range(M):
        if campus[y][x] == 'I':
            visited[y][x] = True
            start = (x, y)
            break

met = 0
q = deque()
q.append(start)

while q:
    for _ in range(len(q)):
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if ny < 0 or ny >= N or nx < 0 or nx >= M:
                continue
            if visited[ny][nx]:
                continue
            if campus[ny][nx] == 'X':
                continue
            visited[ny][nx] = True
            q.append((nx, ny))
            if campus[ny][nx] == 'P':
                met += 1
if met > 0:
    print(met)
else:
    print('TT')