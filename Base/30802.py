import sys

def solution():
    sol1 = sum([num // T if num % T == 0 else num // T + 1 for num in shirts])
    print(sol1)
    print(f"{N // P} {N % P}")

N = int(sys.stdin.readline())
shirts = [int(num) for num in sys.stdin.readline().split()]
T, P = [int(num) for num in sys.stdin.readline().split()]

solution()