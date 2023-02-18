from collections import deque

gear = [deque(map(int, input())) for _ in range(4)]

K = int(input())
rotateInfo = [list(map(int, input().split())) for _ in range(K)]

for i in range(K):
    gearNum, direct = rotateInfo[i]
    q = deque()
    q.append([gearNum, direct])
    visited = [False for _ in range(4)]
    visited[gearNum-1] = True
    while q:
        gearNum, direct = q.popleft()
        if gearNum == 1:
            if gear[0][2] != gear[1][6] and not visited[1]:
                visited[1] = True
                q.append([2, -direct])            
            if direct == 1:
                gear[0].rotate(1)  
            elif direct == -1:
                gear[0].rotate(-1)
            
        elif gearNum == 2:
            if gear[1][2] != gear[2][6] and not visited[2]:
                visited[2] = True
                q.append([3, -direct])
            if gear[1][6] != gear[0][2] and not visited[0]:
                visited[0] = True
                q.append([1, -direct])
            if direct == 1:
                gear[1].rotate(1)  
            elif direct == -1:
                gear[1].rotate(-1)
        elif gearNum == 3:
            if gear[2][2] != gear[3][6] and not visited[3]:
                visited[3] = True
                q.append([4, -direct])
            if gear[2][6] != gear[1][2] and not visited[1]:
                visited[1] = True
                q.append([2, -direct])
            if direct == 1:
                gear[2].rotate(1)  
            elif direct == -1:
                gear[2].rotate(-1)
        elif gearNum == 4:
            if gear[3][6] != gear[2][2] and not visited[2]:
                visited[2] = True
                q.append([3, -direct])            
            if direct == 1:
                gear[3].rotate(1)  
            elif direct == -1:
                gear[3].rotate(-1)

result = 0
for i in range(4):
    if gear[i][0] == 1:
        result += 2 ** i 

print(result)      
