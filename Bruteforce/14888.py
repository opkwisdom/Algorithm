def get_ops_combi(ops):
    ops_combi = []
    def backtrack_op(ops_list, path):
        if len(path) == N-1:
            ops_combi.append(path[:])
            return
        for i in range(4):
            if ops_list[i] > 0:
                ops_list[i] -= 1
                path.append(i)
                backtrack_op(ops_list, path)
                path.pop()  # backtracking 복구 과정
                ops_list[i] += 1
        
    backtrack_op(ops, [])
    return ops_combi
    

def execute_op(a, b, i):
    if i == 0:
        return a+b
    elif i == 1:
        return a-b
    elif i == 2:
        return a*b
    else:
        res = abs(a)//b
        if a < 0:
            res *= -1
        return res
        

N = int(input())
nums = list(map(int, input().split()))
ops = list(map(int, input().split()))   # +, -, *, /

M, m = -10_0000_0000, 10_0000_0000

all_ops = get_ops_combi(ops)
for ops in all_ops:
    res = nums[0]
    for i in range(N-1):
        res = execute_op(res, nums[i+1], ops[i])
    if res > M:
        M = res
    if res < m:
        m = res
        
print(M)
print(m)