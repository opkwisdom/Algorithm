import sys

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

counts = {}
for num in nums:
    if num not in counts.keys():
        counts[num] = 1
    else:
        counts[num] += 1

M = int(sys.stdin.readline())
card_counts = list(map(int, sys.stdin.readline().split()))

for key in card_counts:
    if key in counts.keys():
        print(counts[key], end=' ')
    else:
        print(0, end=' ')
print()