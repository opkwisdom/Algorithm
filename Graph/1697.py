import sys
from collections import deque

N, K = list(map(int, sys.stdin.readline().split()))
result = [0 for _ in range(100001)]

queue = deque()
queue.append(N)

while queue:
    now = queue.popleft()
    if now == K:
        print(result[K])
        break
    for j in (now-1, now+1, now*2):
        if 0 <= j <= 100000 and not result[j] and j != N:
            result[j] = result[now] + 1
            queue.append(j)


# print(result[:K+1])
# print(result[K])