def solution(n, computers):
    def dfs(node, visited, computers):
        visited[node] = True
        for i in range(n):
            if computers[node][i] == 1 and not visited[i]:
                dfs(i,visited,computers)
    
    visited = [False] * n
    count = 0
    
    for i in range(n):
        if not visited[i]:
            dfs(i,visited,computers)
            count += 1
    return count