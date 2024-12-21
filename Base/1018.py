import sys

def compare_board(board1, board2):
    s = 0
    for row1, row2 in zip(board1, board2):
        for i in range(8):
            if (row1[i] != row2[i]):
                s += 1
    return s

# 패턴 생성
pattern1 = "BWBWBWBW"
pattern2 = "WBWBWBWB"

case1 = []
case2 = []

for i in range(8):
    if i % 2 == 0:
        case1.append(pattern1)
        case2.append(pattern2)
    else:
        case1.append(pattern2)
        case2.append(pattern1)

N, M = [int(num) for num in sys.stdin.readline().split()]
board = [sys.stdin.readline().strip() for _ in range(N)]
max_rows = N - 8
max_cols = M - 8

solutions = []
for row_start in range(max_rows+1):
    for col_start in range(max_cols+1):
        sampled = [b[col_start:col_start+8]
                   for b in board[row_start:row_start+8]]
        s1 = compare_board(sampled, case1)
        s2 = compare_board(sampled, case2)
        solutions.extend([s1, s2])

print(min(solutions))