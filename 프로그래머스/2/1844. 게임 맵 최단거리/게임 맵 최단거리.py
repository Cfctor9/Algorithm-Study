from collections import deque

def solution(maps):
    row_len = len(maps)
    col_len = len(maps[0])
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  
    queue = deque([(0, 0, 1)])
    visited = [[False] * col_len for _ in range(row_len)]
    visited[0][0] = True
    
    while queue:
        cur_r, cur_c, count = queue.popleft()        

        if cur_r == row_len - 1 and cur_c == col_len - 1:
            return count        

        for dr, dc in directions:
            next_r = cur_r + dr
            next_c = cur_c + dc
            
            if 0 <= next_r < row_len and 0 <= next_c < col_len and maps[next_r][next_c] == 1 and not visited[next_r][next_c]:
                visited[next_r][next_c] = True
                queue.append((next_r, next_c, count + 1))
    

    return -1


