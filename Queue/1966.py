import sys

def printer(x):
    count = 0
    while True:
        p = priorities.pop(0)

        while True:
            target, idx = nums.pop(0)
            if p > target:
                nums.append((target, idx))
            else:
                count += 1
                break
        if idx == x:
            break
    return count


TC = int(sys.stdin.readline())
for _ in range(TC):
    N, M = list(map(int, sys.stdin.readline().split()))
    nums = [[int(num), i] for i, num in enumerate(sys.stdin.readline().split())]

    priorities = sorted(nums, key=lambda x: x[0], reverse=True)
    priorities = [p[0] for p in priorities]

    print(printer(M))


