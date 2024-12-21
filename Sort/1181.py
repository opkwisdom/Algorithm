import sys

def solution1():
    N = int(input())
    words = {}

    for _ in range(N):
        s = input()
        s_len = len(s)
        
        if s_len not in words.keys():
            words[s_len] = []
        words[s_len].append(s)

    # 중복 제거
    keys = sorted(words.keys())

    for key in keys:
        words[key] = list(set(words[key]))

        if len(words[key]) == 1:
            continue
        # 알파벳 순으로 sort
        else:
            sorted_words = words[key]
            for i in range(key-1, -1, -1):
                sorted_words = sorted(sorted_words, key=lambda x: ord(x[i]))
            words[key] = sorted_words

    # 출력
    for key in keys:
        for word in words[key]:
            print(word)

def solution2():
    N = int(sys.stdin.readline())
    words = list(set([sys.stdin.readline().strip() for _ in range(N)]))
    words.sort()
    print('\n'.join(sorted(words, key=len)))

# solution1()
solution2()