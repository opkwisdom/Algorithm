import sys

def increasing_series(li, s, cnt):
    global result
    if cnt == 0:
        result.append(li)
    if cnt < 0:
        return
    for j in range(s, N):
        nest_li = li.copy()
        nest_li.append(nums[j])
        increasing_series(nest_li, j+1, cnt-1)


result = []
N, M = list(map(int, sys.stdin.readline().split()))
nums = [i for i in range(1, N+1)]
increasing_series([], 0, M)

for res in result:
    print(' '.join([str(i) for i in res]))