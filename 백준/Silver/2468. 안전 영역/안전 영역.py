import sys
sys.setrecursionlimit(100000)  # 재귀 제한 늘리기

def dfs(x,y,height,graph,visited):
    visited[x][y] = True
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and graph[nx][ny] > height:
            dfs(nx,ny,height,graph,visited)

def count_safe_areas(n,height,graph):
    visited = [[False]*n for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and graph[i][j]>height:
                dfs(i,j,height,graph,visited)
                count += 1
    return count

n = int(input())
graph = []
max_height = 0
for i in range(n):
    row = list(map(int,input().split()))
    max_height = max(max_height,max(row))
    graph.append(row)

max_safe_areas = 1
for height in range(max_height):
    safe_areas = count_safe_areas(n,height,graph)
    max_safe_areas = max(max_safe_areas, safe_areas)

print(max_safe_areas)
