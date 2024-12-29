import sys
from collections import deque

N, M = list(map(int, sys.stdin.readline().split()))
ladders = {}
snakes = {}
INF = float('inf')

board = [0 for _ in range(101)]
visited = [False for _ in range(101)]

for _ in range(N):
    x, y = list(map(int, sys.stdin.readline().split()))
    ladders[x] = y
for _ in range(M):
    x, y = list(map(int, sys.stdin.readline().split()))
    snakes[x] = y

q = deque([1])
visited[1] = True
while q:
    x = q.popleft()
    if x == 100:
        print(board[x])
        break
    for i in range(1, 7):
        next_p = x + i
        if next_p <= 100 and not visited[next_p]:
            if next_p in ladders.keys():
                next_p = ladders[next_p]
            if next_p in snakes.keys():
                next_p = snakes[next_p]
            if not visited[next_p]:
                visited[next_p] = True
                board[next_p] = board[x] + 1
                q.append(next_p)

# for i in range(10):
#     print(visited[i*10+1:i*10+11])
# for i in range(10):
#     print(board[i*10+1:i*10+11])