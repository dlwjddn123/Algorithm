def solution(cards):
    visited = [False for _ in range(len(cards))]
    groups = findGroup(cards, visited)
    if len(groups) == 1:
        return 0
    groups.sort(reverse=True)
    return groups[0] * groups[1]

def findGroup(cards, visited):
    groups = []
    for i in range(len(cards)):
        if not visited[i]:
            visited[i] = True
            idx = cards[i] - 1
            count = 1
            while not visited[idx]:
                visited[idx] = True
                count += 1
                idx = cards[idx] - 1
            groups.append(count)
    return groups
        
            
    
        