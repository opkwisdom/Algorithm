def hanoi(n, s, m, t):
    global sol
    if n == 1:
        print(s, t)
        return
    else:
        hanoi(n-1, s, t, m)
        hanoi(1, s, m, t)
        hanoi(n-1, m, s, t)


n = int(input())
sol = 2**n-1
print(sol)
hanoi(n, 1, 2, 3)