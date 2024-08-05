# https://www.acmicpc.net/problem/2023

import sys

N = int(sys.stdin.readline())

candidates = ['2', '3', '5', '7']
# 11, 13, 17, 19, 
def is_prime_num(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def get_candidates(candidates):
    new_candidates = []
    for candidate in candidates:
        for i in range(1, 10):
            n = int(candidate + str(i))
            if is_prime_num(n):
                new_candidates.append(str(n))
    return new_candidates

for i in range(1, N):
    candidates = get_candidates(candidates)
for candidate in candidates:
    print(candidate)