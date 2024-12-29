import sys

def combination(li, is_exist, cnt):
    global result
    check = 0
    if cnt == 0:
        result.append(li)
        return
    for i, exist in enumerate(is_exist):
        if not exist and check != nums[i]:
            nest_li = li.copy()
            nest_exist = is_exist.copy()
            nest_li.append(nums[i])
            nest_exist[i] = True
            check = nums[i]
            combination(nest_li, nest_exist, cnt-1)


N, M = list(map(int, sys.stdin.readline().split()))
nums = list(map(int, sys.stdin.readline().split()))
nums.sort()
is_exist = [False for _ in range(N)]

result = []
combination([], is_exist, M)

for res in result:
    print(*res)