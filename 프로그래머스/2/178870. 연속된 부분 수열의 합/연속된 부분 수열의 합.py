def solution(sequence, k):
    answer = []
    total = 0
    p1 = 0
    p2 = 0
    while p2 < len(sequence) or p1 < p2:
        if total + sequence[p2] > k:
            total -= sequence[p1]
            p1 += 1
            continue
        
        if total + sequence[p2] < k:
            if p2 == len(sequence) - 1:
                break
            total += sequence[p2]
            p2 += 1
            continue

        if total + sequence[p2] == k:
            total += sequence[p2]
            answer.append([p1, p2])
            if p2 == len(sequence) - 1:
                break
            p2 += 1
    answer.sort(key=lambda x : [x[1]-x[0], x[0]])
    return answer[0]