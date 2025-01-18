from collections import deque

def find_min_seq(a, b):
    q = deque([(a, "")])
    visited = [False for _ in range(10000)]
    visited[a] = True

    while q:
        num, seq = q.popleft()
        if num == b:
            return seq
        
        d = num * 2 % 10000
        if not visited[d]:
            visited[d] = True
            q.append((d, seq + 'D'))

        s = (num-1) % 10000
        if not visited[s]:
            visited[s] = True
            q.append((s, seq + 'S'))
        
        l = (num % 1000)*10 + num // 1000
        if not visited[l]:
            visited[l] = True
            q.append((l, seq + 'L'))
        
        r = (num % 10)*1000 + num // 10
        if not visited[r]:
            visited[r] = True
            q.append((r, seq + 'R'))


T = int(input())
result = []

for _ in range(T):
    A, B = map(int, input().split())
    res = find_min_seq(A, B)
    result.append(res)

for res in result:
    print(res)