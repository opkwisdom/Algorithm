import sys

G = {}
colors = {}
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

for _ in range(M):
    a, b = [int(num) for num in sys.stdin.readline().split()]
    G[a] = G.get(a, [])
    G[a].append(b)
    G[b] = G.get(b, [])
    G[b].append(a)

    if a not in colors.keys():
        colors[a] = 'W'
    if b not in colors.keys():
        colors[b] = 'W'

def dfs(G):
    start = 1
    colors[start] = 'G'    # white -> gray
    result = 0

    def dfs_visit(x):
        nonlocal result
        for adj in G[x]:
            if colors[adj] == 'W':
                result += 1
                colors[adj] = 'G'
                dfs_visit(adj)
        colors[x] = 'B'
    dfs_visit(start)
    return result

if M == 0:
    print(0)
else:
    print(dfs(G))