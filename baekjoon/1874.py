# https://www.acmicpc.net/problem/1874

import sys

N = int(sys.stdin.readline())

eles = list(reversed([i + 1 for i in range(N)]))
nums = []
temp = []
stack = [] # DEBUGGING
results = []
flag = True

for i in range(N):
    num = int(sys.stdin.readline())
    if temp and temp[-1] == num:
        n = temp.pop()
        results.append("-")
        continue

    elif temp and temp[-1] > num:
        flag = False
        break

    else:
        while True:
            n = eles.pop()
            results.append("+")
            temp.append(n) # DEBUGGING
            if n == num:
                temp.pop()
                results.append("-")
                break

if flag:
    for result in results:
        print(result)

else:
    print("NO")