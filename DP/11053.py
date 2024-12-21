def lis(A):
    L = [1] * len(A)
    # Find the LIS
    for i in range(1, len(L)):
        subproblems = [L[k] if A[k] < A[i] else 0 for k in range(i)]
        L[i] = 1 + max(subproblems) if subproblems else 1
    return max(L)

N = int(input())
input_data = input()
numbers = list(map(int, input_data.split()))

res = lis(numbers)
print(res)