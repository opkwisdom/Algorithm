import sys

def case1(x, y):
    '''
    ㅁㅁ
    ㅁㅁ
    '''
    if x < 0 or y < 0 or x+1 >= M or y+1 >= N:
        return 0
    return maps[y][x] + maps[y][x+1] + maps[y+1][x] + maps[y+1][x+1]

def case2(x, y):
    '''ㅁㅁㅁㅁ'''
    if x < 0 or y < 0 or x+3 >= M or y >= N:
        return 0
    return maps[y][x] + maps[y][x+1] + maps[y][x+2] + maps[y][x+3]

def case3(x, y):
    '''
    ㅁ
    ㅁ
    ㅁ
    ㅁ
    '''
    if x < 0 or y < 0 or y+3 >= N or x >= M:
        return 0
    return maps[y][x] + maps[y+1][x] + maps[y+2][x] + maps[y+3][x]

def case4(x, y):
    '''
    ㅁ
    ㅁ
    ㅁㅁ
    '''
    if x < 0 or y < 0 or y+2 >= N or x+1 >= M:
        return 0
    return maps[y][x] + maps[y+1][x] + maps[y+2][x] + maps[y+2][x+1]

def case5(x, y):
    '''
      ㅁ
      ㅁ
    ㅁㅁ
    '''
    if x < 0 or y-2 < 0 or y >= N or x+1 >= M:
        return 0
    return maps[y][x] + maps[y][x+1] + maps[y-1][x+1] + maps[y-2][x+1]

def case6(x, y):
    '''
        ㅁ
    ㅁㅁㅁ
    '''
    if x < 0 or y-1 < 0 or y >= N or x+2 >= M:
        return 0
    return maps[y][x] + maps[y][x+1] + maps[y][x+2] + maps[y-1][x+2]

def case7(x, y):
    '''
    ㅁㅁㅁ
        ㅁ
    '''
    if x < 0 or y < 0 or y+1 >= N or x+2 >= M:
        return 0
    return maps[y][x] + maps[y][x+1] + maps[y][x+2] + maps[y+1][x+2]

def case8(x, y):
    '''
    ㅁㅁ
      ㅁ
      ㅁ
    '''
    if x < 0 or y < 0 or y+2 >= N or x+1 >= M:
        return 0
    return maps[y][x] + maps[y][x+1] + maps[y+1][x+1] + maps[y+2][x+1]

def case9(x, y):
    '''
    ㅁㅁ
    ㅁ
    ㅁ
    '''
    if x < 0 or y < 0 or y+2 >= N or x+1 >= M:
        return 0
    return maps[y][x] + maps[y][x+1] + maps[y+1][x] + maps[y+2][x]

def case10(x, y):
    '''
    ㅁㅁㅁ
    ㅁ
    '''
    if x < 0 or y < 0 or y+1 >= N or x+2 >= M:
        return 0
    return maps[y][x] + maps[y][x+1] + maps[y][x+2] + maps[y+1][x]

def case11(x, y):
    '''
    ㅁ
    ㅁㅁㅁ
    '''
    if x < 0 or y < 0 or y+1 >= N or x+2 >= M:
        return 0
    return maps[y][x] + maps[y+1][x] + maps[y+1][x+1] + maps[y+1][x+2]

def case12(x, y):
    '''
      ㅁㅁ
    ㅁㅁ
    '''
    if x < 0 or y-1 < 0 or y >= N or x+2 >= M:
        return 0
    return maps[y][x] + maps[y][x+1] + maps[y-1][x+1] + maps[y-1][x+2]

def case13(x, y):
    '''
    ㅁㅁ
      ㅁㅁ
    '''
    if x < 0 or y < 0 or y+1 >= N or x+2 >= M:
        return 0
    return maps[y][x] + maps[y][x+1] + maps[y+1][x+1] + maps[y+1][x+2]

def case14(x, y):
    '''
    ㅁ
    ㅁㅁ
      ㅁ
    '''
    if x < 0 or y < 0 or y+2 >= N or x+1 >= M:
        return 0
    return maps[y][x] + maps[y+1][x] + maps[y+1][x+1] + maps[y+2][x+1]

def case15(x, y):
    '''
      ㅁ
    ㅁㅁ
    ㅁ
    '''
    if x < 0 or y < 0 or y+2 >= N or x+1 >= M:
        return 0
    return maps[y][x+1] + maps[y+1][x] + maps[y+1][x+1] + maps[y+2][x]

def case16(x, y):
    '''
    ㅁㅁㅁ
      ㅁ
    '''
    if x < 0 or y < 0 or y+1 >= N or x+2 >= M:
        return 0
    return maps[y][x] + maps[y][x+1] + maps[y][x+2] + maps[y+1][x+1]

def case17(x, y):
    '''
      ㅁ
    ㅁㅁ
      ㅁ
    '''
    if x < 0 or y-1 < 0 or y+1 >= N or x+1 >= M:
        return 0
    return maps[y][x] + maps[y][x+1] + maps[y-1][x+1] + maps[y+1][x+1]

def case18(x, y):
    '''
      ㅁ
    ㅁㅁㅁ
    '''
    if x-1 < 0 or y < 0 or y+1 >= N or x+1 >= M:
        return 0
    return maps[y][x] + maps[y+1][x-1] + maps[y+1][x] + maps[y+1][x+1]

def case19(x, y):
    '''
    ㅁ
    ㅁㅁ
    ㅁ
    '''
    if x < 0 or y < 0 or y+2 >= N or x+1 >= M:
        return 0
    return maps[y][x] + maps[y+1][x] + maps[y+2][x] + maps[y+1][x+1]

input = sys.stdin.readline
N, M = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]

cases = [case1, case2, case3, case4, case5, case6, case7,
         case8, case9, case10, case11, case12, case13,
         case14, case15, case16, case17, case18, case19]
value = 0
for j in range(N):
    for i in range(M):
        for case in cases:
            value = max(value, case(i, j))

print(value)