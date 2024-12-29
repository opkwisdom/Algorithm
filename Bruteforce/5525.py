import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
S = sys.stdin.readline().strip()

cnt = 0
matched = 0
correct = 2*N + 1
start, end = 0, 0

while end < M:
    if matched % 2 == 0:
        if S[end] == 'I':
            matched += 1
            end += 1
        else:
            matched = 0
            end += 1
            start = end
    else:
        if S[end] == 'O':
            matched += 1
            end += 1
        else:
            matched = 1
            start = end
            end += 1

    if matched == correct:
        cnt += 1
        start += 2
        matched -= 2

print(cnt)