# https://www.acmicpc.net/problem/11660
import sys 

N, M = [int(x) for x in sys.stdin.readline().split()]

# N * N 행렬 초기화
arr = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

# 행렬 입력 받기
for i in range(1, N + 1):
    arr[i] = [0] + [int(x) for x in input().split(" ")]

dp = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
dp[1][1] = arr[1][1]
# 1행 / 1열 초기화
for i in range(2, N + 1):
    dp[1][i] = dp[1][i - 1] + arr[1][i] 
for i in range(2, N + 1):
    dp[i][1] = dp[i - 1][1] + arr[i][1] 

# 나머지 부분 채우기
for i in range(2, N + 1):
    for j in range(2, N + 1):
        dp[j][i] = dp[j - 1][i] + dp[j][i - 1] + arr[j][i] - dp[j - 1][i - 1]

for i in range(M):
    y1, x1, y2, x2 = [int(x) for x in sys.stdin.readline().split()]
    ans = dp[y2][x2] - dp[y1][x1] - (dp[y1 - 1][x2] - dp[y1 - 1][x1]) - (dp[y2][x1 - 1] - dp[y1][x1 - 1]) + arr[y1][x1]
    print(ans)