import sys
input = sys.stdin.readline
N = int(input())
seq = list(map(int, input().split()))

res1, res2 = [1 for _ in range(N)], [1 for _ in range(N)]
# forward
for i in range(1, N):
    small_list = [res1[j] for j in range(i) if seq[j] < seq[i]]
    res1[i] = max(small_list) + 1 if small_list else 1
# backward
for i in range(N-1, -1, -1):
    small_list = [res2[j] for j in range(N-1, i, -1) if seq[j] < seq[i]]
    res2[i] = max(small_list) + 1 if small_list else 1

sol = 0
for a, b in zip(res1, res2):
    sol = max(sol, a+b)
sol -= 1

print(sol)