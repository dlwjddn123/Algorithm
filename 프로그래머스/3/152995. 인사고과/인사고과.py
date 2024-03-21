def solution(scores):
    answer = 1
    myScore = scores[0]
    scores.sort(key=lambda x : [-x[0], x[1]])
    maxB = 0
    
    for a, b in scores:
        if a > myScore[0] and b > myScore[1]:
            return -1
        if b >= maxB:
            maxB = b
            if a + b > myScore[0] + myScore[1]:
                answer += 1
            
    return answer