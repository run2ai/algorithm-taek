# https://www.acmicpc.net/problem/10986
import sys

N, M = [int(x) for x in sys.stdin.readline().split()]
nums = [int(x) for x in sys.stdin.readline().split()]

ans = 0
residuals = [0 for _ in range(M)]

sum_ = 0

for i, num in enumerate(nums):
    sum_ += num
    residuals[sum_ % M] += 1

for res in residuals:
    ans += (res * (res - 1)) //2
    
ans += residuals[0]
print(ans)