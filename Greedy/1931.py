import sys

N = int(sys.stdin.readline())
t = []
for _ in range(N):
    t.append(tuple(map(int, sys.stdin.readline().split())))
t = sorted(t, key=lambda x: x[0])    
t = sorted(t, key=lambda x: x[1])

sol = 1
cur = t[0]
for appoint in t[1:]:
    if cur[1] <= appoint[0]:
        cur = appoint
        sol += 1
print(sol)
