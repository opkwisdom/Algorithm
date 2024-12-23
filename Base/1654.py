import sys

def binary_search(low, high):
    if low > high:
        return
    mid = (low + high) // 2
    temp = 0
    global res
    for i in lans:
        temp += i // mid
    if temp >= N:
        res = mid
        binary_search(mid+1, high)
    else:
        binary_search(low, mid-1)

K, N = [int(num) for num in sys.stdin.readline().split()]

lans = []
for _ in range(K):
    lans.append(int(input()))

res = 0
max_value = max(lans)
binary_search(0, max_value * 2)
print(res)