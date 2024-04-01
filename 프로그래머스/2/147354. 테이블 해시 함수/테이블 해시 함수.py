def solution(data, col, row_begin, row_end):
    answer = 0
    data.sort(key=lambda x : (x[col-1], -x[0]))
    S = []
    for i in range(row_begin - 1, row_end):
        result = 0
        for j in range(len(data[i])):
            result += data[i][j] % (i+1)
        S.append(result)
    answer = S[0]
    
    for j in range(1, len(S)):
        answer = answer ^ S[j]
    return answer