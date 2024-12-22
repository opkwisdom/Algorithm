import sys

N = int(sys.stdin.readline())

coords = []
for _ in range(N):
    x, y = [int(num) for num in sys.stdin.readline().split()]
    coords.append((x, y))

coords.sort(key=lambda x: x[1])
coords.sort(key=lambda x: x[0])

for coord in coords:
    print(coord[0], coord[1])