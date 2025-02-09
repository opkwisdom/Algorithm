S = input().strip()
stack = []
value = 0
tmp = 1

for i in range(len(S)):
    if S[i] == "(":
        stack.append(S[i])
        tmp *= 2
    elif S[i] == "[":
        stack.append(S[i])
        tmp *= 3

    elif S[i] == ")":
        if not stack or stack[-1] == "[":
            value = 0
            break
        if S[i-1] == "(":
            value += tmp
        stack.pop()
        tmp //= 2
    elif S[i] == "]":
        if not stack or stack[-1] == "(":
            value = 0
            break
        if S[i-1] == "[":
            value += tmp
        stack.pop()
        tmp //= 3
    
if stack:
    print(0)
else:
    print(value)