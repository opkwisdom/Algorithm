import sys

input = sys.stdin.read
data = input().splitlines()
init = data[0].strip()
N = int(data[1])

# Left, Right 스택
left, right = [], []
for s in init:
    left.append(s)

for i in range(2, N+2):
    line = data[i].split()
    if len(line) == 1:
        op = line[0]
    else:
        op, ch = line[0], line[1]

    if op == "L":
        if left:
            right.append(left.pop())
    elif op == "D":
        if right:
            left.append(right.pop())
    elif op == "B":
        if left:
            left.pop()
    elif op == "P":
        left.append(ch)

full = left + right[::-1]
print("".join(full))