# https://www.acmicpc.net/problem/11004

import sys

N, K = sys.stdin.readline().split()

nums = [int(x) for x in sys.stdin.readline().split()]

print(sorted(nums)[int(K) - 1])