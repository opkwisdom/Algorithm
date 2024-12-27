import sys
from collections import deque
sys.setrecursionlimit(10 ** 6)

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs(queue, cnt):
    if not queue:
        return
    
    new_queue = deque()
    while queue:
        x, y = queue.popleft()
        dist[y][x] = cnt
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < M and 0 <= ny < N:
                if dist[ny][nx] == -1 and cities[ny][nx] != 0:
                    if (nx, ny) not in new_queue:
                        new_queue.append((nx, ny))
    bfs(new_queue, cnt+1)

N, M = list(map(int, sys.stdin.readline().split()))
cities = []
for _ in range(N):
    cities.append(list(map(int, sys.stdin.readline().split())))

dist = [[-1 for _ in range(M)] for _ in range(N)]

for i in range(N):
    for j in range(M):
        if cities[i][j] == 0:
            dist[i][j] = 0
        elif cities[i][j] == 2:
            start = (j, i)  # 시작 지점이 (0, 0)이 아닐 수도 있음

queue = deque()
queue.append(start)
bfs(queue, 0)

for d in dist:
    print(' '.join([str(i) for i in d]))