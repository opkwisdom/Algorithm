import sys
input = sys.stdin.readline

# 8
# Jepson no no no no nobody never
# Ashley why ever not
# Marcus no not never nobody
# Bazza no never know nobody
# Hatty why no nobody
# Hatty nobody never know why nobody
# Jepson never no nobody
# Ashley never never nobody no

M = int(input())
humans = set()
conv_log = {}
for _ in range(M):
    human, line = input().strip().split(maxsplit=1)
    line = line.split()
    
    humans.add(human)
    conv_log[human] = conv_log.get(human, {})
    for word in line:
        conv_log[human][word] = conv_log[human].get(word, 0) + 1

# Collect all words spoken
humans = list(humans)
all_words = []
for h in humans:
    all_words.append(set(conv_log[h].keys()))

# Shortest member should be first
all_words.sort(key=lambda x: len(x))

# Common words used in this conversation
common_words = set.intersection(*all_words)

# Add term frequencies
all_infos = []
for word in common_words:
    cnt = 0
    for h in humans:
        cnt += conv_log[h].get(word, 0)
    all_infos.append((cnt, word))

# Sort first with length in descent order, and then sort in alphabetically
all_infos.sort(key=lambda x: x[1])
all_infos.sort(key=lambda x: -x[0])

if all_infos:
    for cnt, word in all_infos:
        print(word)
else:
    print("ALL CLEAR")