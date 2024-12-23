import sys

tc = int(sys.stdin.readline())

all_tcs = []
for _ in range(tc):
    n = int(sys.stdin.readline())
    clothes = {}
    for _ in range(n):
        wear, category = sys.stdin.readline().strip().split()
        clothes[category] = clothes.get(category, 0) + 1
    all_tcs.append(clothes)

for clothes in all_tcs:
    all_wears = clothes.values()

    combis = 1
    for wears in all_wears:
        combis *= (wears + 1)
    print(combis - 1)