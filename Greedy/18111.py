import sys

N, M, B = list(map(int, sys.stdin.readline().split()))
land = []
land_info = {}
for _ in range(N):
    land.append(list(map(int, sys.stdin.readline().split())))

for i in range(N):
    for j in range(M):
        land_info[land[i][j]] = land_info.get(land[i][j], 0) + 1

t = 0
keys = land_info.keys()
keys = sorted(keys)

while len(keys) > 1:
    if B < land_info[keys[0]]:
        updated_key = keys[-1] - 1
        n_blocks = land_info[keys[-1]]
        land_info[updated_key] = land_info.get(updated_key, 0) + n_blocks
        B += n_blocks
        t += 2 * n_blocks
        land_info.pop(keys[-1])
        keys.pop(-1)
        if updated_key != keys[-1]:
            keys.append(updated_key)
    else:
        # 쌓는 게 우선 순위
        if land_info[keys[0]] <= 2 * land_info[keys[-1]]:
            updated_key = keys[0] + 1
            n_blocks = land_info[keys[0]]
            land_info[updated_key] = land_info.get(updated_key, 0) + n_blocks
            B -= n_blocks
            t += n_blocks
            land_info.pop(keys[0])
            keys.pop(0)
            if updated_key != keys[0]:
                keys.insert(0, updated_key)
        else:
            updated_key = keys[-1] - 1
            n_blocks = land_info[keys[-1]]
            land_info[updated_key] = land_info.get(updated_key, 0) + n_blocks
            B += n_blocks
            t += 2 * n_blocks
            land_info.pop(keys[-1])
            keys.pop(-1)
            if updated_key != keys[-1]:
                keys.append(updated_key)

print(t, keys[-1])