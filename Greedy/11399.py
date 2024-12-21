# i번 사람이 돈을 인출하는데 걸리는 시간은 Pi분
# Queue
# 줄을 서 있는 사람의 수 N과 각 사람이 돈을 인출하는데 걸리는 시간 Pi가 주어졌을 때,
# 각 사람이 돈을 인출하는데 필요한 시간의 합의 최솟값을 구하는 프로그램

N = int(input())
a = [int(num) for num in input().split()]
a = sorted(a)   # O(NlogN)
times = [sum(a[:i]) for i in range(1, N+1)]
print(sum(times))