import sys

N = int(sys.stdin.readline())
nums = [i for i in range(1, N+1)]

start = 0
end = N

while end - start > 1:
    start += 1
    nums.append(nums[start])
    start += 1
    end += 1

print(nums[start])