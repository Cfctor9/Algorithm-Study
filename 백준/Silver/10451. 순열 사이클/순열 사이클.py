def make_graph(n,perm):
    graph = [[] for _ in range(n+1)]
    for i in range(1,n+1):
        graph[i].append(perm[i-1])
    return graph

def dfs(graph, start, visited):
    stack = [start]
    while stack:
        current = stack.pop()
        if not visited[current]:
            visited[current] = True
            stack.extend(i for i in graph[current] if not visited[i])

def make_result(n,perm):
    graph = make_graph(n,perm)
    visited = [False]*(n+1)
    cnt = 0
    for i in range(1,n+1):
        if not visited[i]:
            dfs(graph,i,visited)
            cnt += 1
    return cnt
        
t = int(input())
for _ in range(t):
    n = int(input())
    perm = list(map(int,input().split()))
    result = make_result(n,perm)
    print(result)