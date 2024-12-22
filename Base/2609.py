import sys

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def lcm(a, b):
    g = gcd(a, b)
    return g * (a // g) * (b // g)

a, b = [int(num) for num in sys.stdin.readline().split()]

sol1 = gcd(a, b)
sol2 = lcm(a, b)
print(sol1)
print(sol2)