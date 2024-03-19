def solution(sequence, k):
    answer = None
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
            if answer == None:
                answer = [p1, p2]
            else:
                if (answer[1] - answer[0]) > (p2 - p1):
                    answer = [p1, p2]
            if p2 == len(sequence) - 1:
                break
            p2 += 1
    return answer