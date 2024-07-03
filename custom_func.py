def show_2darray(arr):
    M = len(arr)
    N = len(arr[0])

    for i in range(M):
        for j in range(N):
            print(f"{arr[i][j]} ", end="")
        print("")

if __name__ == '__main__':
    N = 3
    # N * N 행렬 초기화
    arr = [[0 for _ in range(N)] for _ in range(N)]

    # 행렬 입력 받기
    for i in range(N):
        arr[i] = [int(x) for x in input().split(" ")]

    show_2darray(arr)