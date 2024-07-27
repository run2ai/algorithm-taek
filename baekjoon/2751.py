# https://www.acmicpc.net/problem/2751

import sys

N = int(sys.stdin.readline())

nums = [0 for _ in range(N)]

for i in range(N):
    n = int(sys.stdin.readline())
    nums[i] = n
    
for num in sorted(nums):
    print(num)
