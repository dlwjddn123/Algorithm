N, K = map(int, input().split())
arr = list(map(int, input()))
result = [arr[0]]
cK = K
for i in range(1, N):
    while cK > 0 and len(result) > 0 and arr[i] > result[-1]:
            result.pop()
            cK -= 1
    result.append(arr[i])

for i in range(N-K):
    print(result[i], end="")
