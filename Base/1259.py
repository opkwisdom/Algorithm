import sys

def solution(nums):
    for num in nums:
        i, j = 0, len(num)-1
        while i < j:
            if num[i] != num[j]:
                break
            i += 1
            j -= 1
        
        if i < j:
            print("no")
        else:
            print("yes")

nums = []
while True:
    num = sys.stdin.readline().strip()
    if num == "0":
        break
    nums.append(num)
solution(nums)
