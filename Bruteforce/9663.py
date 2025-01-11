def N_Queen(r): # r: 놓은 말의 수
    global n, cnt
    if r == n:
        cnt += 1
        return
    
    for c in range(n):
        if not used_c[c] and not used_up[r+c] and not used_down[r-c]:
            used_c[c] = True
            used_up[r+c] = True
            used_down[r-c] = True
            N_Queen(r+1)
            used_c[c] = False
            used_up[r+c] = False
            used_down[r-c] = False


n = int(input())
used_c = [False for _ in range(n)]  # 1. 열 방향
used_up = [False for _ in range(2*n-1)]    # 2. y=x 방향
used_down = [False for _ in range(2*n-1)]    # 3. y=-x 방향
cnt = 0

N_Queen(0)
print(cnt)