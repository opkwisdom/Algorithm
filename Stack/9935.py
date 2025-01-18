seq = input().strip()
bomb = input().strip()
t = len(bomb)

stack = []
for i in range(len(seq)):
    stack.append(seq[i])
    if "".join(stack[-t:]) == bomb:
        for _ in range(t):
            stack.pop()

if not stack:
    print("FRULA")
else:
    print("".join(stack))