import sys

N, M = list(map(int, sys.stdin.readline().split()))
A = set()
for _ in range(N):
    A.add(sys.stdin.readline().strip())
B = set()
for _ in range(M):
    B.add(sys.stdin.readline().strip())

A = list(A.intersection(B))
A.sort()
print(len(A))
for element in A:
    print(element)