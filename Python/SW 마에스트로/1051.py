N, M = map(int, input().split())
square = [list(map(int, input())) for _ in range(N)]
size = []
result = []
for i in range(0, min(N, M)):
    size.append(i)

def go(l):
    for i in range(N-l):
        for j in range(M-l):
           if square[i][j] == square[i+l][j] == square[i][j+l] == square[i+l][j+l]:
               result.append((l+1)*(l+1))

for n in size:
    go(n)
print(max(result))

