import sys
from collections import deque
sys.setrecursionlimit(10 ** 6)
# 1 : 익은 토마토, 0 : 익지 않은 토마토, -1 : 비어 있는 칸

def bfs():
    answer = 0

    q = deque()
    for y in range(N):
        for x in range(M):
            if tomatoes[y][x] == 1:
                q.append((y, x))

    while q:
        for _ in range(len(q)):
            y, x = q.popleft()
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if ny < 0 or ny >= N or nx < 0 or nx >= M:
                    continue
                if tomatoes[ny][nx] == 0:
                    tomatoes[ny][nx] = 1
                    q.append((ny, nx))
        if q:
            answer += 1

    return answer


dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

# N X M
M, N = list(map(int, sys.stdin.readline().split()))
tomatoes = []
for _ in range(N):
    tomatoes.append(list(map(int, sys.stdin.readline().split())))

answer = bfs()

amateur_exist = False
for y in range(N):
    for x in range(M):
        if tomatoes[y][x] == 0:
            amateur_exist = True
            break
if amateur_exist:
    answer = -1

print(answer)

