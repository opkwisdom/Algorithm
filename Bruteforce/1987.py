dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def can_move(x, y):
    return  (x >= 0 and x < C) and (y >= 0 and y < R)

def alphabet(start):
    max_visit = 1
    x, y = start
    container = set()
    container.add(board[y][x])
    stack = [(start, 1, container)]

    while stack:
        (x, y), cnt, visited = stack.pop()
        max_visit = max(max_visit, cnt)

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if can_move(nx, ny):
                if board[ny][nx] not in visited:
                    new_visited = visited.copy()
                    new_visited.add(board[ny][nx])
                    stack.append(((nx, ny), cnt+1, new_visited))
    return max_visit


R, C = map(int, input().split())
board = []
for _ in range(R):
    board.append(input().strip())

sol = alphabet((0, 0))
print(sol)