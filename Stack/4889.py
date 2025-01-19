import sys
input = sys.stdin.readline

P = []
while True:
    line = input().strip()
    if line[0] == '-':
        break
    P.append(line)

result = []
for data in P:
    cnt = 0
    stack = []
    for i in range(len(data)):
        if data[i] == '{':
            stack.append(data[i])
        else:
            if stack:
                stack.pop()
            else:
                cnt += 1
                stack.append('{')
    if stack:
        cnt += (len(stack) // 2)
    result.append(cnt)

for i, res in enumerate(result):
    print(f'{i+1}. {res}')