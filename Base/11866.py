n,k = map(int,input().split())
arr = [i for i in range(1,n+1)]

idx = 0
print('<',end='')
for i in range(n-1):
  idx=(idx+k-1)%(n-i)
  print(arr.pop(idx), end=', ')

print(arr[0],end='>')