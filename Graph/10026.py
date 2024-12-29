import sys
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs_regular(x, y):
    global sector1, cnt1
    q = deque()
    q.append((x, y))
    cnt1 += 1
    sector1[y][x] = cnt1

    c = paint[y][x]
    while q:
        for _ in range(len(q)):
            x, y = q.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if nx < 0 or nx >= N or ny < 0 or ny >= N:
                    continue
                if not sector1[ny][nx] and paint[ny][nx] == c:
                    sector1[ny][nx] = cnt1
                    q.append((nx, ny))

def bfs_irregular(x, y):
    global sector2, cnt2
    q = deque()
    q.append((x, y))
    cnt2 += 1
    sector2[y][x] = cnt2

    c = paint[y][x]
    is_green_or_red = c != 'B'
    while q:
        for _ in range(len(q)):
            x, y = q.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if nx < 0 or nx >= N or ny < 0 or ny >= N:
                    continue
                if not sector2[ny][nx]:
                    if is_green_or_red:
                        if paint[ny][nx] != 'B':
                            sector2[ny][nx] = cnt2
                            q.append((nx, ny))
                    else:
                        if paint[ny][nx] == 'B':
                            sector2[ny][nx] = cnt2
                            q.append((nx, ny))


paint = []
N = int(sys.stdin.readline())
for _ in range(N):
    paint.append(sys.stdin.readline().strip())

sector1 = [[0 for _ in range(N)] for _ in range(N)]
sector2 = [[0 for _ in range(N)] for _ in range(N)]
cnt1, cnt2 = 0, 0

for y in range(N):
    for x in range(N):
        if sector1[y][x] == 0:
            bfs_regular(x, y)
        if sector2[y][x] == 0:
            bfs_irregular(x, y)

print(cnt1, cnt2)