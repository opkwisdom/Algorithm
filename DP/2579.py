def stepping_stairs(scores, N):
    values = []
    for i in range(N+1):
        values.append([0, 0])
    values[1][0] = scores[0]

    for j in range(2, N+1):
        values[j][0] = scores[j-1] + max(values[j-2])
        values[j][1] = scores[j-1] + values[j-1][0]
    
    return max(values[N])

N = int(input())
scores = []
for i in range(N):
    scores.append(int(input()))

res = stepping_stairs(scores, N)
print(res)