def star_pattern(k):
    if k == 0:
        return ["  *  ", " * * ", "*****"]

    prev_pattern = star_pattern(k-1)
    size = len(prev_pattern)
    # print(size)

    top, bottom = [], []
    for i, row in enumerate(prev_pattern):
        top_pattern = " " * size + row + " " * size
        bottom_pattern = row + " " + row
        top.append(top_pattern)
        bottom.append(bottom_pattern)
    return top + bottom


n = int(input())
k = 0
n //= 3
while n > 1:
    n //= 2
    k += 1
stars = star_pattern(k)

for row in stars:
    print(row)
