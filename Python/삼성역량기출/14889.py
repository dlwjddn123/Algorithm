from os import link


N = int(input())
M = [[0] for _ in range(N+1)]
answer = 101
for i in range(1, N+1):
    n = map(int, input().split())
    M[i] += n
visited = [0 for _ in range(N+1)]
def dfs(idx, cnt):
    global answer
    if cnt == N // 2:
        linksum = 0
        startsum = 0
        for i in range(1,N+1):
            for j in range(1, N+1):
                if i == j:
                    continue
                elif visited[i] and visited[j]:
                    startsum += M[i][j]
                elif not visited[i] and not visited[j]:
                    linksum += M[i][j]

        answer = min(answer, abs(startsum - linksum))

    for i in range(idx, N+1):
        if visited[i]:
            continue
        visited[i] = 1
        dfs(i + 1, cnt + 1)
        visited[i] = 0

dfs(1, 0)
print(answer)    
