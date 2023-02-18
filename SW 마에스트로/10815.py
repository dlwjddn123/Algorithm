N = int(input())
cards = list(map(int, input().split()))
cards.sort()
M = int(input())
nums = list(map(int, input().split()))
result = []
for n in nums:
    start, end = 0, len(cards)
    answer = 0
    while start <= end:
        mid = (start+end) // 2
        if cards[mid] > n:
            end = mid - 1
        if cards[mid] < n:
            start = mid + 1
        if cards[mid] == n:
            answer = 1
            break
    result.append(answer)

print(result)
