import sys

print(sum([int(num)**2 for num in sys.stdin.readline().split()]) % 10)