import sys
from collections import deque

dy = [0, -1, 0, 1]
dx = [-1, 0, 1, 0]

N = int(sys.stdin.readline())
apart = []
for _ in range(N):
    apart.append(sys.stdin.readline().strip())

apart_tag = [[0 for _ in range(N)] for _ in range(N)]
tag = 0
q = deque()
tag_nums = []

for y in range(N):
    for x in range(N):
        if not apart_tag[y][x] and apart[y][x] == '1':
            tag += 1
            apart_tag[y][x] = tag
            num = 1
            q.append((y,x))
            while q:
                for _ in range(len(q)):
                    tmp_y, tmp_x = q.popleft()
                    for i in range(4):
                        ny, nx = tmp_y + dy[i], tmp_x + dx[i]
                        if ny < 0 or ny >= N or nx < 0 or nx >= N:
                            continue
                        if not apart_tag[ny][nx] and apart[ny][nx] == '1':
                            apart_tag[ny][nx] = tag
                            num += 1
                            q.append((ny, nx))
            tag_nums.append(num)

tag_nums.sort()

print(tag)
for num in tag_nums:
    print(num)