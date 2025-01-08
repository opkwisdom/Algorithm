from collections import deque
from copy import deepcopy

INF = float('inf')

N, M = map(int, input().split())
town = []
for _ in range(N):
    town.append(list(map(int, input().split())))

# 집, 치킨집 select
houses = []
chickens = []
for r in range(N):
    for c in range(N):
        if town[r][c] == 1:
            houses.append((r, c))
        elif town[r][c] == 2:
            chickens.append((r, c))


def chicken_delivery(start, selected):
    global chickens, city_dist
    if len(selected) == M:
        dist = calculate_dist(selected)
        city_dist = min(city_dist, dist)
        return

    for i in range(start, len(chickens)):
        chicken_delivery(i+1, selected + [chickens[i]])

def calculate_dist(selected_chickens):
    dist = 0
    for r1, c1 in houses:
        tmp_dist = INF
        for r2, c2 in selected_chickens:
            tmp_dist = min(tmp_dist, (abs(r1-r2)+abs(c1-c2)))
        dist += tmp_dist
    return dist

city_dist = INF
chicken_delivery(0, [])
print(city_dist)
##### TC ######
# 1.
# 5 2
# 0 2 0 1 0
# 1 0 1 0 0
# 0 0 0 0 0
# 2 0 0 1 1
# 2 2 0 1 2

# 2.
# 5 3
# 0 0 1 0 0
# 0 0 2 0 1
# 0 1 2 0 0
# 0 0 1 0 0
# 0 0 0 0 2