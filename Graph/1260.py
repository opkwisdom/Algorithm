import sys
sys.setrecursionlimit(10 ** 6)

def dfs(G, colors, V):
    result = [V]
    if V not in G.keys():
        return result
    
    colors[V] = 'G'
    
    def dfs_visit(G, colors, V):
        for adj in G[V]:
            if colors[adj] == 'W':
                colors[adj] = 'G'
                result.append(adj)
                dfs_visit(G, colors, adj)
        colors[V] = 'B'
    dfs_visit(G, colors, V)

    return result

def bfs(G, colors, V):
    result = [V]
    if V not in G.keys():
        return result
    Q = [V]
    colors[V] = 'G'
    
    while Q:
        cur = Q.pop(0)
        for adj in G[cur]:
            if colors[adj] == 'W':
                colors[adj] = 'G'
                Q.append(adj)
                result.append(adj)
        colors[cur] = 'B'

    return result


N, M, V = list(map(int, sys.stdin.readline().split()))
G = {}
colors = {}
for _ in range(M):
    a, b = list(map(int, sys.stdin.readline().split()))
    G[a] = G.get(a, [])
    G[a].append(b)
    G[b] = G.get(b, [])
    G[b].append(a)

for key in G.keys():
    colors[key] = 'W'
    G[key] = sorted(G[key])

dfs_result = dfs(G.copy(), colors.copy(), V)
bfs_result = bfs(G.copy(), colors.copy(), V)

print(' '.join([str(r) for r in dfs_result]))
print(' '.join([str(r) for r in bfs_result]))