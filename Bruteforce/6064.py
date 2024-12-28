import sys

#     A = kM + x , A = lN + y
# <=> kM = lN + y - x
# <=> (lN + y - x) mod M == 0 ... (from i=0 to M)

sols = []
tc = int(sys.stdin.readline())
for _ in range(tc):
    M, N, x, y = list(map(int, sys.stdin.readline().split()))

    isFound = False
    for i in range(M):
        if (i*N + y - x) % M == 0:
            A = i*N + y
            sols.append(A)
            isFound = True
            break
        
    if not isFound:
        sols.append(-1)

for sol in sols:
    print(sol)