import sys # max함수로 한번 찾는 게 max변수로 값 계속 비교하는 것보다 훨씬 빠름..
input = sys.stdin.readline

N, M = map(int, input().split())
cards = sorted(list(map(int, input().split())))[::-1]

result = []
for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            if cards[i] + cards[j] + cards[k] <= M:
                result.append(cards[i] + cards[j] + cards[k])
                break


print(max(result))