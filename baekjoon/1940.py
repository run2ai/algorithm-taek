# https://www.acmicpc.net/problem/1940

import sys
from collections import defaultdict

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

nums = [int(x) for x in sys.stdin.readline().split()]

num_dict = defaultdict(int)
cnt = 0

for num in nums:
    num_dict[num] += 1
    
for i in range((M + 1) // 2):
    cnt += min(num_dict[i], num_dict[M - i])

print(cnt)
