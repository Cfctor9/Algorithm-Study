import sys
sys.setrecursionlimit(10**6)

def dfs(x, visited, perm):
    visited[x] = True
    next = perm[x-1]
    if not visited[next]:
        dfs(next, visited, perm)

for _ in range(int(input())):
    n = int(input())
    perm = list(map(int, input().split()))
    visited = [False] * (n+1)
    cnt = 0
    
    for i in range(1, n+1):
        if not visited[i]:
            dfs(i, visited, perm)
            cnt += 1
    print(cnt)