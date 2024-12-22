import sys

# 최적은 dict 사용 (O(1))
# Binary search : O(logN)
def binary_search(As, num, left, right):
    while left <= right:
        mid = (left + right) // 2
        if As[mid] == num:
            return 1
        elif As[mid] > num:
            right = mid-1
        else:
            left = mid+1
    return 0

N = int(sys.stdin.readline().strip())
As = list(map(int, sys.stdin.readline().split()))
As.sort()

M = int(sys.stdin.readline().strip())
Bs = list(map(int, sys.stdin.readline().split()))

for num in Bs:
    print(binary_search(As, num, 0, N-1))