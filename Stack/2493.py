import sys
input = sys.stdin.readline
N = int(input())
top = list(map(int, input().split()))
result = [0 for _ in range(N)]

stack = []
for i in range(N-1, -1, -1):
    while stack and stack[-1][0] <= top[i]:
        h, pos = stack.pop()
        result[pos] = i+1
    stack.append((top[i], i))

print(*result)