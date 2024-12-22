import sys

M = int(sys.stdin.readline())
S = set()

for _ in range(M):
    line = sys.stdin.readline().split()
    
    if len(line) == 1:
        execution = line[0]
    else:
        execution = line[0]
        num = int(line[1])

    if execution == "add":
        S.add(num)
    elif execution == "remove":
        if num in S:
            S.remove(num)
    elif execution == "check":
        if num in S:
            print(1)
        else:
            print(0)
    elif execution == "toggle":
        if num in S:
            S.remove(num)
        else:
            S.add(num)
    elif execution == "all":
        S = set([i for i in range(1, 21)])
    else:
        S.clear()