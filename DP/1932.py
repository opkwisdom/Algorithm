def integer_triangle(nums, N):
    V = []
    for i in range(N+1):
        V.append([0] * (N+1))

    # import pdb; pdb.set_trace();
    for j in range(1, N+1):
        for i in range(1, j+1):
            V[i][j] = max(V[i-1][j-1], V[i][j-1]) + nums[j-1][i-1]

    return max(V[i][N] for i in range(1, N+1))

N = int(input())

total_nums = []
for i in range(N):
    data = input()
    nums = list(map(int, data.split()))
    total_nums.append(nums)

print(integer_triangle(total_nums, N))