def exist_messy_room(y, x):
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if can_move(ny, nx) and not maps[ny][nx]:
            return True
    return False

def can_move(y, x):
    return (x >= 0 and y >= 0) and (y < N and x < M) and maps[y][x] != 1

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

N, M = map(int, input().split())
r, c, d = map(int, input().split())
maps = []
for _ in range(N):
    maps.append(list(map(int, input().split())))

cnt = 0
while True:
    # Action 1
    if not maps[r][c]:
        maps[r][c] = 2
        cnt += 1
    
    # Action 3
    if exist_messy_room(r, c):
        for i in range(4):
            nd = (d-1-i)%4    # 반시계 회전
            nr, nc = r+dy[nd], c+dx[nd]
            if can_move(nr, nc) and not maps[nr][nc]:
                r, c, d = nr, nc, nd
                break
    # Action 2
    else:
        b_d = (d-2)%4
        nr, nc = r+dy[b_d], c+dx[b_d]
        if can_move(nr, nc):
            r, c = nr, nc
        else:
            break

print(cnt)
