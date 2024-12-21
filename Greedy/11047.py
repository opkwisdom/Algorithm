# N종류의 동전으로 가치 K를 만드는 데 필요한 최소 동전 개수
# A_1=1, A_i는 A_{i-1}의 배수

def process_coins(coins, K):
    coins = [coin for coin in coins if coin <= K]
    max_index = 0
    for i, coin in enumerate(coins):
        if K % coin != 0:
            max_index = i-1
            break
    coins = coins[max_index:]
    
    return coins

def minimum_coins(coins, K):
    coins = process_coins(coins, K)
    if K in coins:
        return 1

    solution = 0
    idx = len(coins) - 1
    while K > 0 and idx >= 0:
        solution += (K // coins[idx])
        K  %= coins[idx]
        idx -= 1

    return solution


N, K = [int(a) for a in input().split()]

coins = []
for i in range(N):
    coins.append(int(input()))

print(minimum_coins(coins, K))
