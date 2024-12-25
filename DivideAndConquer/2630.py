import sys

def ColorPaper(x, y, N):
    global whites, blues
    tmp_cnt = 0
    
    for i in range(x, x+N):
        for j in range(y, y+N):
            if board[i][j]:
                tmp_cnt += 1
    if not tmp_cnt:
        whites += 1
    elif tmp_cnt == N**2:
        blues += 1
    else:
        mid = N // 2
        ColorPaper(x, y, mid)
        ColorPaper(x + mid, y, mid)
        ColorPaper(x, y + mid, mid)
        ColorPaper(x + mid, y + mid, mid)
    return

N = int(sys.stdin.readline())
board = []
for _ in range(N):
    line = list(map(int, sys.stdin.readline().split()))
    board.append(line)

whites = 0
blues = 0
ColorPaper(0, 0, N)
print(whites)
print(blues)