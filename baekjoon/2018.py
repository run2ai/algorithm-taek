# https://www.acmicpc.net/problem/2018
import sys

N = int(sys.stdin.readline())

start = 1
end = 1
ans = 1
s = 1

while end != N:
    if s < N:
        end += 1
        s += end
        continue
    
    if s > N:
        s -= start
        start += 1
        continue
    
    if s == N:
        ans += 1
        end += 1
        s += end
        continue

print(ans)

        