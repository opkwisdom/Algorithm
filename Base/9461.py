def pado(num):
    result = [0, 1, 1, 1, 2, 2, 3]

    for i in range(7, num+1):
        result.append(result[i-1] + result[i-5])
    return result[num]

T = int(input())

Ns = []
for _ in range(T):
    Ns.append(int(input()))

for num in Ns:
    print(pado(num))