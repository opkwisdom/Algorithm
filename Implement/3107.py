# 25:09:1985:aa:091:4846:374:bb
# 0025:0009:1985:00aa:0091:4846:0374:00bb
# ::1
# 0000:0000:0000:0000:0000:0000:0000:0001

line = input().strip().split(':')
n = 0
for i in range(len(line)):
    if line[i] != '':
        n += 1

if len(line) > 8:
    if line[0] == '':
        line = line[1:]
    elif line[-1] == '':
        line = line[:-1]

ipv6 = []
if n < 7:
    for i in range(8):
        if line[i] == '':
            cur = i
            break
        else:
            ipv6.append(line[i])
    
    for i in range(n, 8):
        ipv6.append('0000')
    
    for i in range(cur+1, len(line)):
        if line[i] != '':
            ipv6.append(line[i])
else:
    ipv6 = line[:]

for i in range(8):
    if len(ipv6[i]) < 4:
        ipv6[i] = '0'*(4-len(ipv6[i])) + ipv6[i]

print(':'.join(ipv6))