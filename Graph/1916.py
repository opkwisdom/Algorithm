import heapq

INF = float("inf")
N = int(input())
M = int(input())

G = {i: [] for i in range(1, N + 1)}

# 그래프 입력
for _ in range(M):
    u, v, w = list(map(int, input().split()))
    G[u].append((w, v))

s, d = map(int, input().split())
# Relaxation
dist = [INF for _ in range(N+1)]
dist[s] = 0
heap = [(0, s)]

# import pdb; pdb.set_trace();
while heap:
    cur_dist, cur_node = heapq.heappop(heap)
    # cur_dist가 dist[cur_node]보다 더 크다는 뜻은 relaxation 끝났다는 것
    if cur_dist > dist[cur_node]:
        continue
    for w, u in G[cur_node]:
        # Relaxation
        cost = cur_dist + w
        if dist[u] > cost:
            dist[u] = cost
            heapq.heappush(heap, (cost, u))

print(dist[d])
# for row in dist:
#     print(row)
