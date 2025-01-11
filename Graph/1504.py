import heapq

INF = float('inf')

def dijkstra(s):
    dist = [INF for _ in range(N+1)]
    dist[s] = 0
    heap = [(s, 0)]   # 시작

    while heap:
        v, d = heapq.heappop(heap) # Min-heap에서 최솟값 꺼내기
        if dist[v] < d:
            continue
        for u, w in G[v]:
            cost = d + w
            if dist[u] > cost:
                dist[u] = cost
                heapq.heappush(heap, (u, cost))
    return dist


N, E = map(int, input().split())
G = {i: [] for i in range(1, N+1)}  # Undirected weighted graph

for _ in range(E):
    v, u, w = map(int, input().split())
    G[v].append((u, w))
    G[u].append((v, w))
i1, i2 = map(int, input().split())  # 반드시 지나야 하는 정점 두 개

P1 = dijkstra(1)     # 1. 1번 노드에 대한 다익스트라
P2 = dijkstra(i1)    # 2. imp1번 노드에 대한 다익스트라
P3 = dijkstra(i2)    # 3. imp2번 노드에 대한 다익스트라
min_dist = min(P1[i1]+P2[i2]+P3[N],
               P1[i2]+P3[i1]+P2[N])
print(min_dist if min_dist < INF else -1)
# print(f"Shortest Path from 1: {P1}")
# print(f"Shortest Path from {i1}: {P2}")
# print(f"Shortest Path from {i2}: {P3}")