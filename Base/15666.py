import sys

def combination(li, cur, cnt):
    global result
    check = 0
    if cnt == 0:
        result.append(li)
        return
    while cur < N:
        if check != nums[cur]:
            nest_li = li.copy()
            nest_li.append(nums[cur])
            check = nums[cur]
            combination(nest_li, cur, cnt-1)
        cur += 1

N, M = list(map(int, sys.stdin.readline().split()))
nums = list(map(int, sys.stdin.readline().split()))
nums.sort()

result = []
combination([], 0, M)

for res in result:
    print(*res)