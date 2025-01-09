from collections import deque

def can_move(state, head):
    tmp_y, tmp_x = head
    if state == 'right':
        return space[tmp_y][tmp_x+1] != 1
    elif state == 'lower-right':
        return (space[tmp_y][tmp_x+1] != 1
                and space[tmp_y+1][tmp_x] != 1
                and space[tmp_y+1][tmp_x+1] != 1)
    else:
        return space[tmp_y+1][tmp_x] != 1

# DFS 방법 => 시간 초과
# def move_pipe(state, head, trace):
#     '''
#     state: {'right', 'lower-right', 'down'}
#     head: head pos of pipe
#     '''
#     global sol
#     if head == [N-1, N-1]:
#         sol += 1
#         # print(trace)
#         return
    
#     y, x = head
    
#     if state == 'right':
#         if x+1 < N and can_move('right', head):
#             new_state, new_head = 'right', [y, x+1]
#             move_pipe(new_state, new_head, trace + ['right'])
#         if (y+1 < N and x+1 < N) and can_move('lower-right', head):
#             new_state, new_head = 'lower-right', [y+1, x+1]
#             move_pipe(new_state, new_head, trace + ['lower-right'])
#     elif state == 'lower-right':
#         if x+1 < N and can_move('right', head):
#             new_state, new_head = 'right', [y, x+1]
#             move_pipe(new_state, new_head, trace + ['right'])
#         if (y+1 < N and x+1 < N) and can_move('lower-right', head):
#             new_state, new_head = 'lower-right', [y+1, x+1]
#             move_pipe(new_state, new_head, trace + ['lower-right'])
#         if y+1 < N and can_move('down', head):
#             new_state, new_head = 'down', [y+1, x]
#             move_pipe(new_state, new_head, trace + ['down'])
#     else:
#         if (y+1 < N and x+1 < N) and can_move('lower-right', head):
#             new_state, new_head = 'lower-right', [y+1, x+1]
#             move_pipe(new_state, new_head, trace + ['lower-right'])
#         if y+1 < N and can_move('down', head):
#             new_state, new_head = 'down', [y+1, x]
#             move_pipe(new_state, new_head, trace + ['down'])

N = int(input())
space = []
for _ in range(N):
    space.append(list(map(int, input().split())))

sol = 0
DP = [[[0 for _ in range(N)]
       for _ in range(N)]
       for _ in range(3)]

DP[0][0][1] = 1
for i in range(2,N):
    if space[0][i] == 0:
        DP[0][0][i] = DP[0][0][i - 1]

for i in range(1,N):
    for j in range(1,N):
        if space[i][j] == 0 and space[i][j - 1] == 0 and space[i - 1][j] == 0:
            DP[2][i][j] = DP[0][i - 1][j - 1] + DP[1][i - 1][j - 1] + DP[2][i - 1][j - 1]
            # 대각선 파이프 놓기

        if space[i][j] == 0:
            DP[0][i][j] = DP[0][i][j - 1] + DP[2][i][j - 1]
            # 가로 파이프 놓기

            DP[1][i][j] = DP[1][i - 1][j] + DP[2][i - 1][j]
            # 세로 파이프 놓기
print(DP[0][N - 1][N - 1] + DP[1][N - 1][N - 1] + DP[2][N - 1][N - 1])
# move_pipe('right', head, ['right'])
# print(sol)

# TC1
# 5
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0
# TC2
# 6
# 0 0 0 0 0 0
# 0 1 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
