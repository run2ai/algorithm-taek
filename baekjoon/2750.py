# https://www.acmicpc.net/problem/2750

import sys

N = int(sys.stdin.readline())

nums = []
for _ in range(N):
    nums.append(int(sys.stdin.readline()))

for num in sorted(nums):
    print(num)