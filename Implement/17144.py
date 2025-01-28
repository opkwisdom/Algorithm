import sys
input = sys.stdin.readline

dy = [0, -1, 0, 1]
dx = [-1, 0, 1, 0]

def can_move(room, x, y):
    return (x >= 0 and x < C) and (y >= 0 and y < R) and room[y][x] != -1

def diffuse(pre_room):
    diffused_room = [[0 for _ in range(C)] for _ in range(R)]

    for y in range(R):
        for x in range(C):
            if pre_room[y][x] == -1:
                diffused_room[y][x] = -1
                continue

            if pre_room[y][x] > 0:  # There exist finedust
                amount = pre_room[y][x] // 5
                n = 0
                # 인접 4방향 탐색
                for i in range(4):
                    nx, ny = x+dx[i], y+dy[i]
                    if can_move(pre_room, nx, ny):
                        diffused_room[ny][nx] += amount
                        n += 1
                rest = pre_room[y][x] - n * amount
                diffused_room[y][x] += rest

    return diffused_room

def purify(room, loc1, loc2):
    # 위쪽 공기청정기 (반시계 방향)
    t_x, t_y = loc1
    for y in range(t_y-1, 0, -1):
        room[y][0] = room[y-1][0]
    for x in range(0, C-1):
        room[0][x] = room[0][x+1]
    for y in range(0, t_y):
        room[y][C-1] = room[y+1][C-1]
    for x in range(C-1, 1, -1):
        room[t_y][x] = room[t_y][x-1]
    room[t_y][1] = 0

    # 아래쪽 공기청정기 (시계 방향)
    t_x, t_y = loc2
    for y in range(t_y+1, R-1):
        room[y][0] = room[y+1][0]
    for x in range(0, C-1):
        room[R-1][x] = room[R-1][x+1]
    for y in range(R-1, t_y, -1):
        room[y][C-1] = room[y-1][C-1]
    for x in range(C-1, 0, -1):
        room[t_y][x] = room[t_y][x-1]
    
    room[t_y][1] = 0

    return room


R, C, T = map(int, input().split())
room = []
for _ in range(R):
    room.append(list(map(int, input().split())))

# 공기청정기 위치 찾기
isFound = False
for y in range(R):
    for x in range(C):
        if room[y][x] == -1:
            loc1 = (x, y)
            loc2 = (x, y+1)
            isFound = True
            break
    if isFound:
        break

# T번 반복
for _ in range(T):
    room = diffuse(room)
    room = purify(room, loc1, loc2)

# 미세먼지 양 체크
total = 0
for y in range(R):
    for x in range(C):
        if room[y][x] > 0:
            total += room[y][x]
print(total)
