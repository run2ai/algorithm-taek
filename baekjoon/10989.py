# https://www.acmicpc.net/problem/10989

import sys
from collections import defaultdict

N = int(sys.stdin.readline())
num_dict = defaultdict(int)

for _ in range(N):
    num = int(sys.stdin.readline())
    num_dict[num] += 1

for num in list(sorted(num_dict.keys())):
    for _ in range(num_dict[num]):
        print(num)