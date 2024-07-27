# https://www.acmicpc.net/problem/11399

import sys

from collections import defaultdict

N = int(sys.stdin.readline())
num_dict = defaultdict(int)

times = [int(x) for x in sys.stdin.readline().split(' ')]

tot_time = 0
wait_time = 0
for time in sorted(times):
    tot_time += time
    tot_time += wait_time
    wait_time += time
    
print(tot_time)