from collections import deque

INF = float('inf')
N, K = map(int, input().split())

max_pos = 100000
dp = [INF for _ in range(max_pos+1)]
visited = [False for _ in range(max_pos+1)]
dp[N] = 0
visited[N] = True

q = deque([N])
while q:
    # Teleport
    for _ in range(len(q)):
        i = q.popleft()
        pos = i
        if not pos:
            q.append(i)
            continue
        while pos <= max_pos:
            if not visited[pos]:
                dp[pos] = dp[i]
                q.append(pos)
                visited[pos] = True
            pos *= 2
        q.append(i)
    # Walk
    for _ in range(len(q)):
        i = q.popleft()
        if i > 0 and not visited[i-1]:
            dp[i-1] = dp[i] + 1
            visited[i-1] = True
            q.append(i-1)
        if i < max_pos and not visited[i+1]:
            dp[i+1] = dp[i] + 1
            visited[i+1] = True
            q.append(i+1)
    if visited[K]:
        break

print(dp[K])