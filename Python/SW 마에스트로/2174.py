from collections import deque

A, B = map(int, input().split())
field = [[0]*(A) for _ in range(B)]
direct = [[0, 1], [-1, 0], [0, -1], [1, 0]] 
N, M = map(int ,input().split())

robot = [[]]
robotDirect = [deque()]
for i in range(N):
    x, y, d = input().split()
    q = deque()
    for i in range(4):
        q.append(direct[i])    
    if d == "S":
        q.rotate(-3)
    elif d == "W":
        q.rotate(-2)
    elif d == "N":
        q.rotate(-1)
    robot.append([int(x)-1, B-int(y)])
    robotDirect.append(q)
for i in range(1, N+1):
    field[robot[i][1]][robot[i][0]] = i

commands = []
for _ in range(M):
    robotNum, command, count = input().split()
    commands.append([int(robotNum), command, int(count)])
result = ""

def go():
    global result
    for i in range(M):
        if commands[i][1] == 'L':
            robotDirect[commands[i][0]].rotate(-commands[i][2])
        if commands[i][1] == 'R':
            robotDirect[commands[i][0]].rotate(commands[i][2])
        if commands[i][1] == 'F':
            for j in range(commands[i][2]):
                x, y = robot[commands[i][0]][0], robot[commands[i][0]][1]
                nx, ny = x + robotDirect[commands[i][0]][0][1], y + robotDirect[commands[i][0]][0][0]
                if not (0 <= nx < A and 0 <= ny < B):
                    result = "Robot "+ str(commands[i][0]) + " crashes into the wall"
                    return
                elif field[ny][nx] != 0: 
                    result = "Robot " + str(commands[i][0]) + " crashes into robot " + str(field[ny][nx])
                    return 
                robot[commands[i][0]][0], robot[commands[i][0]][1] = nx, ny
                field[ny][nx] = commands[i][0]
                field[y][x] = 0

    result = "OK"
    return 
go()
print(result)

