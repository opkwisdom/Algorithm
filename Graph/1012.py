import sys
sys.setrecursionlimit(10**6)

def makeSet(i, j):
    global setId
    global farm
    global setIds
    global colors
    
    setId += 1
    setIds[i][j] = setId
    colors[i][j] = 'G'
    
    def dfs_visit(i, j):
        setIds[i][j] = setId
        conts = [[-1, 0], [0, -1], [1, 0], [0, 1]]
        for cont in conts:
            x, y = i + cont[0], j + cont[1]
            if (x >= 0 and x < M) and (y >= 0 and y < N) and\
                farm[x][y] == 1 and colors[x][y] == 'W':
                colors[x][y] = 'G'
                dfs_visit(x, y)
        colors[i][j] = 'B'
    dfs_visit(i, j)


T = int(sys.stdin.readline())
solutions = []

for _ in range(T):
    M, N, K = list(map(int, sys.stdin.readline().split()))

    farm = [[0 for _ in range(N)] for _ in range(M)]
    colors = [['W' for _ in range(N)] for _ in range(M)]
    setIds = [[-1 for _ in range(N)] for _ in range(M)]

    for _ in range(K):
        i, j = list(map(int, sys.stdin.readline().split()))
        farm[i][j] = 1

    setId = 0
    for col in range(N):
        for row in range(M):
            if farm[row][col] == 1 and colors[row][col] == 'W':
                makeSet(row, col)
    solutions.append(setId)

for id in solutions:
    print(id)