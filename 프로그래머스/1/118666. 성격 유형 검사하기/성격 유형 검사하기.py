def solution(survey, choices):
    answer = ''
    scores = dict()
    scores['T'], scores['R'], scores['C'], scores['F'] = 0, 0, 0, 0
    scores['J'], scores['M'], scores['A'], scores['N'] = 0, 0, 0, 0
    
    for i in range(len(survey)):
        if choices[i] == 4:
            continue
        type1, type2 = survey[i][0], survey[i][1]
        if choices[i] < 4:
            scores[type1] += 4 - choices[i]
        else:
            scores[type2] += choices[i] - 4
    
    if scores['T'] > scores['R']:
        answer += 'T'
    else:
        answer += 'R'
    
    if scores['F'] > scores['C']:
        answer +='F'
    else:
        answer +='C'
    
    if scores['M'] > scores['J']:
        answer += 'M'
    else:
        answer += 'J'
    
    
    if scores['N'] > scores['A']:
        answer += 'N'
    else:
        answer += 'A'
    
    return answer