import sys
sys.setrecursionlimit(10**8)

def dfs(start, now): # 가장 먼 지점 찾기
    for child, w in G[start]:
        if visited[child] == -1:
            visited[child] = w + now
            dfs(child, visited[child])

n = int(input())
G = [[] for _ in range(n+1)]
for _ in range(n-1):
    u, v, w = map(int, input().split())
    G[u].append((v, w))
    G[v].append((u, w))

# 루트 노드 (Node 1)부터 dfs
visited = [-1 for _ in range(n+1)]
visited[1] = 0
dfs(1, 0)

# 가장 먼 노드 v1에 대해 다시 bfs
v1 = visited.index(max(visited))
visited = [-1 for _ in range(n+1)]
visited[v1] = 0
dfs(v1, 0)

print(max(visited))