# https://www.acmicpc.net/problem/7453

import sys

N = int(sys.stdin.readline())

arr = [[0 for _ in range(4)] for _ in range(N)]
for i in range(N):
    row = [int(x) for x in sys.stdin.readline().split()]

    arr[i] = row

a, b, c, d = 0, 0, 0, 0

ans = 0

def get_min_diff(idx_list, arr):
    candidates = []
    for i, x in enumerate(idx_list):
        if x == N - 1:
            candidates.append(999)
            continue
        
        if x < N - 1:
            candidates.append(abs(sum(arr[x]) + arr[x + 1][i]))
        
    min_ = 999
    min_idx = -1
    for i, cand in enumerate(candidates):
        if cand < min_:
            min_ = cand
            min_idx = i
    
    return min_idx

idx_list = [0, 0, 0, 0]

while all([x < N for x in idx_list]):
    sum_ = sum([arr[idx_list[x]][x] for x in range(4)])
    if sum_ == 0:
        ans += 1
    
    else:
        min_idx = get_min_diff(idx_list, arr)
        idx_list[min_idx] += 1
        print(idx_list, min_idx, ans, sum_)
print(ans)