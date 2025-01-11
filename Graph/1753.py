import heapq

INF = 1e9

V, E = map(int, input().split())
s = int(input())
G = [[] for _ in range(V + 1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    G[u].append((v, w))

dist  = [INF for _ in range(V+1)]
dist[s] = 0
heap = []
heapq.heappush(heap, (0, s))

while heap:
    d, v = heapq.heappop(heap)
    if d > dist[v]:
        continue
    for u, w in G[v]:
        cost = w + d
        if dist[u] > cost:
            dist[u] = cost
            heapq.heappush(heap, (cost, u))

for d in dist[1:]:
    print(d if d < INF else "INF")