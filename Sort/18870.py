import sys

N = int(sys.stdin.readline())

# 압축 위함
X_dict = {}
for i, num in enumerate(map(int, sys.stdin.readline().split())):
    X_dict[num] = X_dict.get(num, [])
    X_dict[num].append(i)

keys = X_dict.keys()
sorted_keys = sorted(keys)

result = [-1 for _ in range(N)]
for i, key in enumerate(sorted_keys):
    for num in X_dict[key]:
        result[num] = i

print(' '.join(map(str, result)))