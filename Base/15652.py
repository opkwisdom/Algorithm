import sys

def increasing_series(li, cur, cnt):
    global result
    if cnt == 0:
        result.append(li)
        return
    if cnt < 0:
        return
    while cur < N:
        nest_li = li.copy()
        nest_li.append(nums[cur])
        increasing_series(nest_li, cur, cnt-1)
        cur += 1


result = []
N, M = list(map(int, sys.stdin.readline().split()))
nums = [i for i in range(1, N+1)]
increasing_series([], 0, M)

for res in result:
    print(' '.join([str(i) for i in res]))