import sys

def combination(li, is_contained, cnt):
    global result
    if cnt == 0:
        result.append(li)
        return
    
    for i, exist in enumerate(is_contained):
        if not exist:
            nest_li = li.copy()
            nest_contained = is_contained.copy()
            nest_li.append(nums[i])
            nest_contained[i] = True
            combination(nest_li, nest_contained, cnt-1)

result = []
N, M = list(map(int, sys.stdin.readline().split()))
nums = list(map(int, sys.stdin.readline().split()))
is_contained = [False for _ in range(N)]
nums.sort()

combination([], is_contained, M)
for res in result:
    print(' '.join([str(i) for i in res]))
