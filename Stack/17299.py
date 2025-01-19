import sys
input = sys.stdin.readline

N = int(input())
seq = list(map(int, input().strip().split()))
count = {}
# count
for num in seq:
    count[num] = count.get(num, 0) + 1

# stack
result = [-1 for _ in range(N)]
stack = []
for i in range(N):
    while stack and count[stack[-1][0]] < count[seq[i]]:
        num, pos = stack.pop()
        result[pos] = seq[i]
    stack.append((seq[i], i))

print(*result)