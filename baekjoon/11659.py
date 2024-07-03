# https://www.acmicpc.net/problem/11659

M, N = [int(x) for x in input().split(" ")]
nums = [int(x) for x in input().split(" ")]
for _ in range(N):
    i, j = [int(x) for x in input().split(" ")]
    sum_ = sum(nums[i-1:j])
    print(sum_)