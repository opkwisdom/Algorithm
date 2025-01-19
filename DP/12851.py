from collections import deque

MAX_POS = 100000

def can_move(p):
    return p >= 0 and p <= MAX_POS

N, K = map(int, input().split())
visited = [0 for _ in range(MAX_POS+1)]
q = deque([N])

n_way, min_count = 0, None
while q:
    pos = q.popleft()
    cnt = visited[pos]
    if pos == K:
        min_count = cnt
        n_way += 1
        continue
    for new_pos in [pos-1, pos+1, 2*pos]:
        # 방문하지 않았거나, 현재 방문+1 == 이전 방문 횟수 일때
        if can_move(new_pos) and (not visited[new_pos] or cnt+1 == visited[new_pos]):
            visited[new_pos] = cnt+1
            q.append(new_pos)

if N == K:
    print(0)
    print(1)
else:
    print(min_count)
    print(n_way)
