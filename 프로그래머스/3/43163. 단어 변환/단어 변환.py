from collections import deque
def solution(begin, target, words):
    if target not in words:
        return 0
    queue = deque([(begin,0)])
    visited = set()
    
    while queue:
        current_word,current_step = queue.popleft()
        
        if current_word == target:
            return current_step
        
        for word in words:
            if word not in visited and sum(1 for a,b in zip(current_word,word) if a!=b ) == 1:
                visited.add(word)
                queue.append((word, current_step+1))
    return 0
    
    