# https://www.acmicpc.net/problem/11660
N, M = [int(x) for x in input().split(" ")]

# N * N 행렬 초기화
arr = [[0 for _ in range(N)] for _ in range(N)]

# 행렬 입력 받기
for i in range(N):
    arr[i] = [int(x) for x in input().split(" ")]


for i in range(M):
    # x1,y1,x2,y2 입력
    x1, y1, x2, y2 = [int(x) for x in input().split(" ")]

    # 합 구하기 -> 슬라이싱으로 좀 더 예쁘게 될 듯
    sum_ = 0
    
    for y in range(y1 - 1, y2):
        sum_+= sum(arr[y][x1 - 1:x2])

    print(sum_)