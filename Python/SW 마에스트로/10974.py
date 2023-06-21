N = int(input())
temp = []
visited = []
def go(current):
    if len(temp) == N:
        print(*temp)
        return
    for i in range(1, N+1):
        if i not in visited:
            visited.append(i)
            temp.append(i)
            go(i)
            temp.pop()
            visited.pop()

go(0)