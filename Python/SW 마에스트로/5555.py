A = input()
N = int(input())
rings = [input() for _ in range(N)]
result = 0
for i in range(len(rings)):
    rings[i] += rings[i]
    if A in rings[i]:
        result += 1
        continue

print(result)