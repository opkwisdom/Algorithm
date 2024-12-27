import sys

def search(x, y, L):
    if L == 0:
        return
    
    global sector_tracker
    mid = 2 ** (L - 1)

    if r < y + mid and c < x + mid:
        sector_tracker.append(0)
        search(x, y, L-1)
    elif r < y + mid and c >= x + mid:
        sector_tracker.append(1)
        search(x+mid, y, L-1)
    elif r >= y + mid and c < x + mid:
        sector_tracker.append(2)
        search(x, y+mid, L-1)
    elif r >= y + mid and c >= x + mid:
        sector_tracker.append(3)
        search(x+mid, y+mid, L-1)


N, r, c = list(map(int, sys.stdin.readline().split()))
sector_tracker = []
search(0, 0, N)

order = 0
for i in range(N-1, -1, -1):
    order += sector_tracker[N-1-i] * ((2 ** i) ** 2)

print(order)