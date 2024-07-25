# https://www.acmicpc.net/problem/1427

import sys
from collections import defaultdict

N = sys.stdin.readline()[:-1]

num_dict = defaultdict(int)

for num in list(N):
    num_dict[int(num)] += 1

ans = ''
for num in reversed(range(10)):
    ans += str(num) * num_dict[num]

print(ans)