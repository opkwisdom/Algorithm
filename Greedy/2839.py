# 3kg, 5kg 봉지
# 최대한 적은 봉지를 들고 가는 방법
# ex) 18kg -> 5 * 3 + 3 * 1 => 4
# 3 <= N <= 5000

def sugar_delivery(N):
    if N <= 5:
        if N == 3 or N == 5:
            return 1
        else:
            return -1

    methods = [-1] * (N+1)
    methods[3] = methods[5] = 1 # Base case

    for i in range(6, N+1):
        if methods[i-3] > 0 and methods[i-5] > 0:
            methods[i] = min(methods[i-3], methods[i-5]) + 1
        elif methods[i-3] > 0:
            methods[i] = methods[i-3] + 1
        elif methods[i-5] > 0:
            methods[i] = methods[i-5] + 1

    return methods[N]

N = int(input())
print(sugar_delivery(N))

# testcases = [18, 4, 6, 9, 11]

# for tc in testcases:
    # print(f"{sugar_delivery(tc)}")