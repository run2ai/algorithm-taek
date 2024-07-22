# https://www.acmicpc.net/problem/2164

import sys

from collections import deque

N = int(sys.stdin.readline())

queue = deque(list(range(1, N + 1)))

cnt = 0
while len(queue) > 1:
    if cnt % 2 == 0:
        queue.popleft()
    else:
        num = queue.popleft()
        queue.append(num)

    cnt += 1
print(queue[0])