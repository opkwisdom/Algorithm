import sys
import heapq


heap = []
result = []
N = int(sys.stdin.readline())
for _ in range(N):
    x = int(sys.stdin.readline())

    if x == 0:
        if not heap:
            result.append(0)
        else:
            result.append(-heapq.heappop(heap))
    else:
        heapq.heappush(heap, -x)

for x in result:
    print(x)
