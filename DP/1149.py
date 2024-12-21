def painting_houses(costs, N):
    C = []
    for i in range(N+1):
        C.append([0, 0, 0])
    C[1] = costs[0]

    for j in range(2, N+1):
        fill_costs(C[j], C[j-1], costs[j-1])

    return min(C[N])

def fill_costs(cur, prev, cost):
    cur[0] = min(prev[1], prev[2]) + cost[0]
    cur[1] = min(prev[0], prev[2]) + cost[1]
    cur[2] = min(prev[0], prev[1]) + cost[2]

N = int(input())

total_nums = []
for i in range(N):
    num_input = input()
    numbers = list(map(int, num_input.split()))
    total_nums.append(numbers)

cost = painting_houses(total_nums, N)
print(cost)