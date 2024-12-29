import sys
from collections import deque

dx = [0, 0, -1, 1, 0, 0]
dy = [0, 0, 0, 0, -1, 1]
dz = [1, -1, 0, 0, 0, 0]

M, N, H = list(map(int, sys.stdin.readline().split()))
boxes = []
for _ in range(H):
    box = []
    for _ in range(N):
        box.append(list(map(int, sys.stdin.readline().split())))
    boxes.append(box)

q = deque()
# 시작 지점 찾기
for z in range(H):
    for y in range(N):
        for x in range(M):
            if boxes[z][y][x] == 1:
                q.append((x, y, z))

days = 0
while q:
    for _ in range(len(q)):
        x, y, z = q.popleft()
        for i in range(6):
            nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]
            if (nz < 0 or nz >= H) or (ny < 0 or ny >= N) or (nx < 0 or nx >= M):
                continue
            if boxes[nz][ny][nx] == 0:
                boxes[nz][ny][nx] = 1
                q.append((nx, ny, nz))
    if q:
        days += 1

for z in range(H):
    for y in range(N):
        for x in range(M):
            if boxes[z][y][x] == 0:
                days = -1
                break
print(days)