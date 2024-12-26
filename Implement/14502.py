import sys
from collections import deque
import copy
# sys.setrecursionlimit(10 ** 6)

# 4 directions
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

# bfs : 시간 초과남
def diffuse_virus():
    queue = deque()
    tmp_board = copy.deepcopy(board)

    for i in range(N):
        for j in range(M):
            if board[i][j] == 2:
                queue.append((i, j))
    
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            tmp_y = y + dy[i]
            tmp_x = x + dx[i]
            # 확산 가능
            if 0 <= tmp_x < M and 0 <= tmp_y < N:
                if tmp_board[tmp_y][tmp_x] == 0:
                    tmp_board[tmp_y][tmp_x] = 2
                    queue.append((tmp_y, tmp_x))
    
    global answer
    cnt = 0

    for i in range(N):
        cnt += tmp_board[i].count(0)

    answer = max(answer, cnt)

# def diffuse_virus():
#     tmp_board = copy.deepcopy(board)
#     tmp_colors = copy.deepcopy(colors)

#     queue = deque()
#     for i in range(N):
#         for j in range(M):
#             if board[i][j] == 2:
#                 queue.append((i, j))

#     def dfs_visit(x, y):
#         tmp_board[y][x] = 2
#         tmp_colors[y][x] = 'G'
#         for i in range(4):
#             tmp_y = y + dy[i]
#             tmp_x = x + dx[i]
#             # 확산 가능
#             if 0 <= tmp_x < M and 0 <= tmp_y < N:
#                 if tmp_board[tmp_y][tmp_x] != 1 and tmp_colors[tmp_y][tmp_x] == 'W':
#                     dfs_visit(tmp_x, tmp_y)
#         tmp_colors[y][x] = 'B'

#     for y, x in queue:
#         if tmp_colors[y][x] == 'W':
#             dfs_visit(x, y)
    
#     global answer
#     cnt = 0
#     for i in range(N):
#         cnt += tmp_board[i].count(0)
    
#     answer = max(answer, cnt)
    


def make_wall(cnt):
    if cnt == 3:
        diffuse_virus()
        return
    
    for i in range(N):
        for j in range(M):
            if board[i][j] == 0:
                board[i][j] = 1
                make_wall(cnt + 1)
                board[i][j] = 0

N, M = list(map(int, sys.stdin.readline().split()))
board = []
for _ in range(N):
    line = list(map(int, sys.stdin.readline().split()))
    board.append(line)
colors = [['W' for _ in range(M)] for _ in range(N)]

answer = 0
make_wall(0)

print(answer)