import sys

T = int(sys.stdin.readline())
result = []

for _ in range(T):
    cmd = sys.stdin.readline().strip()
    n = int(sys.stdin.readline())
    nums = eval(sys.stdin.readline())

    direction = 'F'
    f_ptr, r_ptr = 0, n-1
    deleted = 0
    error_occured = False

    for op in cmd:
        if op == 'R':
            direction = 'B' if direction == 'F' else 'F'
        else:
            if direction == 'F':
                while f_ptr == -1 and f_ptr < n:
                    f_ptr += 1
                if f_ptr >= n:
                    error_occured = True
                    break
                else:
                    nums[f_ptr] = -1
                    f_ptr += 1
                    deleted += 1
            else:
                while r_ptr == -1 and r_ptr >= 0:
                    r_ptr -= 1
                if r_ptr < 0:
                    error_occured = True
                    break
                else:
                    nums[r_ptr] = -1
                    r_ptr -= 1
                    deleted += 1
    if deleted > n:
        error_occured = True

    if error_occured:
        result.append('error')
    else:
        selected = []
        if direction == 'F':
            for i in range(n):
                if nums[i] != -1:
                    selected.append(nums[i])
        else:
            for i in range(n-1, -1, -1):
                if nums[i] != -1:
                    selected.append(nums[i])
        result.append(selected)


for res in result:
    if res != 'error':
        print(f"[{','.join([str(i) for i in res])}]")
    else:
        print('error')

