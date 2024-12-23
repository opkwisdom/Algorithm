import sys

N, M = [int(num) for num in sys.stdin.readline().split()]

pws = {}
for _ in range(N):
    site, pw = sys.stdin.readline().strip().split()
    pws[site] = pw

sites = []
for _ in range(M):
    sites.append(sys.stdin.readline().strip())
for site in sites:
    print(pws[site])