# https://www.acmicpc.net/problem/11286

import sys

from queue import PriorityQueue
N = int(sys.stdin.readline())

que = PriorityQueue()
for _ in range(N):
    n = int(sys.stdin.readline())
    if n != 0:
        que.put((abs(n), n))

    if n == 0:
        if que.qsize() > 0:
            print(que.get()[1])
        else:
            print(0)