N = int(input())
honey = list(map(int, input().split()))

honeyPrefixSum = honey[:]
honeySurfixSum = honey[:]

for i in range(1, N):
    honeyPrefixSum[i] += honeyPrefixSum[i-1]

for i in range(2, N+1):
    honeySurfixSum[-i] += honeySurfixSum[-i+1]

maxHoney = 0

# 왼쪽
for i in range(1, N-1):
    temp = (honeyPrefixSum[-1] - honey[0] - honey[i]) + (honeyPrefixSum[-1] - honeyPrefixSum[i])
    if maxHoney < temp:
        maxHoney = temp
        
# 오른쪽
for i in range(1, N-1):
    temp = (honeySurfixSum[0] - honey[-1] - honey[-i-1]) + (honeySurfixSum[0] - honeySurfixSum[-i-1])
    if maxHoney < temp:
        maxHoney = temp

# 양 끝
for i in range(1, N-1):
    temp = (honeyPrefixSum[i] - honey[0]) + (honeySurfixSum[i] - honey[-1])
    if maxHoney < temp:
        maxHoney = temp

print(maxHoney)

