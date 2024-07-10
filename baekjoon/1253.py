# https://www.acmicpc.net/problem/1253

import sys

N = int(sys.stdin.readline())

nums = [int(x) for x in sys.stdin.readline().split()]

nums.sort()

ans = 0
for  i, goal in enumerate(nums):
    start = 0
    end = len(nums) - 1
    # start가 end보다 작을 때까지반 loop 돌리기
    while start < end:
        # end, start의 합이 goal일 경우
        if nums[start] + nums[end] == goal:
            # start, end에 goal이 포함될 경우 제외
            if start == i:
                start += 1
                continue
            if end == i:
                end -= 1
                continue
            if start != i and end != i:
                ans += 1
                break
        # start, end의 합이 goal보다 클 경우
        if nums[start] + nums[end] > goal:
            end -=1 
            continue
        # start, end의 합이 goal보다 작을 경우
        if nums[start] + nums[end] < goal:
            start += 1
            continue
print(ans)