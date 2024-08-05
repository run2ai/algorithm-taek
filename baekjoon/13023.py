# https://www.acmicpc.net/problem/13023

import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# dfs 함수
def dfs(graph, v, visited, cnt):
    visited[v] = True
    if cnt == 4:
        return 4
    
    for i in graph[v]:
        if not visited[i]:
            cnt += 1
            dfs(graph, i, visited, cnt)

n, m = map(int, input().split()) # 정점의 개수, 간선의 개수
graph = [[] for _ in range(n+1)]
for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

count = 0 # 연결 노드의 수
visited = [False] * (n+1)
for i in range(1, n+1):
    if not visited[i]:
        cnt = 0
        cnt = dfs(graph, i, visited, cnt)
        count += 1 # dfs 한 번 끝날 때마다 count+1
        print(cnt)
print(count)