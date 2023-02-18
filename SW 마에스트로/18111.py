import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())

house = [list(map(int, input().split())) for _ in range(N)]
heights = []
total = B
for i in range(N):
    for j in range(M):
        heights.append(house[i][j])
        total += house[i][j]

lowsest = min(heights)
highst = max(heights)
if highst > 256:
    highst = 256
result = []
def go(h):
    t = 0
    blockCount = total
    print(f"높이 : {h}")
    for i in range(N):
        for j in range(M):
            blockCount -= house[i][j]
            print(blockCount)
            print(f"시간 : {t}")
            if blockCount < 0:
                return
            if house[i][j] > h:
                t += (house[i][j] - h) * 2
                blockCount += house[i][j] - h
                continue
            

            if house[i][j] < h:
                print(f"blockCount : {blockCount}, h - house[i][j] : {h - house[i][j]}")
                if blockCount - (h - house[i][j]) < 0 :
                    return 
                t += h - house[i][j]
                blockCount -= (h - house[i][j])
                continue
            
    result.append([t, h])

for h in range(lowsest, highst+1):
    go(h)
result.sort(key=lambda x : x[0])
print(result)
answer = result[0]
for i in range(len(result)):
    if result[i][0] == answer[0] and result[i][1] > answer[1]:
        answer = result[i]
        continue
    if result[i][0] != answer[0]:
        break
print(*answer) 
    
        