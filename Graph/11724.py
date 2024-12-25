import sys
sys.setrecursionlimit(10 ** 6)

def dfs(G, node):
    global n_comps
    n_comps += 1
    colors[node] = 'G'
    
    if node not in G.keys():
        colors[node] = 'B'
        return
    
    def dfs_visit(u):
        for adj in G[u]:
            if colors[adj] == 'W':
                colors[adj] = 'G'
                dfs_visit(adj)
        colors[u] = 'B'
    dfs_visit(node)

N, M = list(map(int, sys.stdin.readline().split()))
G = {}
colors = ['W' for _ in range(N+1)]

for _ in range(M):
    u, v = list(map(int, sys.stdin.readline().split()))
    G[u] = G.get(u, [])
    G[u].append(v)
    G[v] = G.get(v, [])
    G[v].append(u)

n_comps = 0
for i in range(1, N+1):
    if colors[i] == 'W':
        dfs(G, i)

print(n_comps)