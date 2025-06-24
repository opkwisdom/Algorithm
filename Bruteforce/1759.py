def get_combinations(char_list, n):
    combi = []
    
    def backtrack(start, path):
        if len(path) == n:
            combi.append(path[:])   # 복사본 저장
            return
        for i in range(start, len(char_list)):
            path.append(char_list[i])
            backtrack(i+1, path)
            path.pop()
    backtrack(0, [])
    
    return combi

def make_crypto(v_num, c_num):
    v_combi = get_combinations(V, v_num)
    c_combi = get_combinations(C, c_num)
    
    for vc in v_combi:
        for cc in c_combi:
            crypto_l = sorted(vc + cc)
            crypto = ''.join(crypto_l)
            crypto_list.append(crypto)
    return

vowel_list = ['a', 'e', 'i', 'o', 'u']

l, c = map(int, input().split())
chars = input().split()

crypto_list = []
V, C = [], []

for char in chars:
    if char in vowel_list:
        V.append(char)
    else:
        C.append(char)
V.sort()
C.sort()

for v_num in range(1, len(V)+1):
    c_num = l - v_num
    if c_num < 2:
        break
    make_crypto(v_num, c_num)

crypto_list.sort()
for crypto in crypto_list:
    print(crypto)