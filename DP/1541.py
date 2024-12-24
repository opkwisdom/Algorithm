import sys

_input = sys.stdin.readline().strip()

_input = _input.split('-')
isFirstNegative = False

if _input[0] == '':
    _input.pop(0)
    isFirstNegative = True
number_list = [list(map(int, a.split('+'))) for a in _input]

total = sum(number_list[0])
if isFirstNegative:
    total *= -1

for i in range(1, len(number_list)):
    total -= sum(number_list[i])
print(total)
