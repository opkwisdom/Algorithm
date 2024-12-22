import sys

r = 31
M = 1234567891
base = ord('a') - 1

N = int(sys.stdin.readline())
string = sys.stdin.readline().strip()

s = 0
for i in range(N):
    s += (ord(string[i]) - base) * (r ** i)
print(s % M)