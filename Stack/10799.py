row = input()
stack = []
cnt = 0
for i in range(len(row)):
    if row[i] == "(":
        stack.append("(")
    else:
        if row[i-1] == "(":
            stack.pop()
            cnt += len(stack)   # 레이저가 지나감
        else:
            stack.pop()
            cnt += 1    # 쇠막대기의 끝부분
print(cnt)