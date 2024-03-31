result = []

def solution(k, dungeons):
    answer = -1
    find(k, dungeons, 0, [False for _ in range(len(dungeons))])
    if len(result) == 0:
        return 0
    answer = max(result)
    return answer

def find(k, dungeons, count, visited):
    if k < 0:
        result.append(count-1)
        return
    elif k == 0:
        result.append(count)
        return
    elif count >= len(dungeons):
        result.append(count)
        return
    
    for i in range(len(dungeons)):
        if visited[i]:
            continue
        
        if k >= dungeons[i][0]:
            visited[i] = True
            find(k - dungeons[i][1], dungeons, count + 1, visited)
            visited[i] = False
            
    result.append(count)
    return
    