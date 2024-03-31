from collections import deque

def solution(x, y, n):
    if x == y:
        return 0
    
    answer = find(x, y, n)

    return answer

def find(x, y, n):
    visited = [False for _ in range(y+1)]
    queue = deque()
    queue.append([x, 1])
    
    while queue:
        x, count = queue.popleft()
        temp = [x + n, x * 2, x * 3]
        
        for nx in temp:
            if nx == y:
                return count
            elif nx < y and not visited[nx]:
                visited[nx] = True
                queue.append([nx, count + 1])
    
    return -1
                
            
        
            
    