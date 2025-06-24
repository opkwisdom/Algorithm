from itertools import combinations

def get_score(A):
    score = 0
    combis = combinations(A, 2)
    for i, j in combis:
        score += (S[i][j] + S[j][i])
    return score

def get_min_diff():
    min_diff = float('inf')
    indices = [i for i in range(N)]
    groups = combinations(indices, N//2)
    for A in groups:
        B = indices[:]
        for n in A:
            B.remove(n)
        diff = abs(get_score(A) - get_score(B))
        if diff < min_diff:
            min_diff = diff
            
    return min_diff
    

N = int(input())

S = []
for i in range(N):
    line = list(map(int, input().split()))
    S.append(line)

min_diff = get_min_diff()
print(min_diff)