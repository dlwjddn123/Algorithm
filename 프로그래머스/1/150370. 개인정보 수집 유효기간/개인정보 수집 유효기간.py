def solution(today, terms, privacies):
    answer = []
    y, m, d = today.split(".")
    today = [int(y), int(m), int(d)]
    termsMap = dict()
    
    for term in terms:
        type, expirationMonth = term.split()
        termsMap[type] = int(expirationMonth)
    
    for i in range(len(privacies)):
        date, type = privacies[i].split()
        y, m, d = date.split(".")
        date = [int(y), int(m), int(d)]

        date[0] += termsMap[type] // 12
        date[1] += termsMap[type] % 12
        date[2] -= 1
        
        if date[1] > 12:
            date[0] += 1
            date[1] -= 12
        if date[2] == 0:
            date[1] -= 1
            date[2] = 28
            if date[1] == 0:
                date[0] -= 1
                date[1] = 12
        
        if today[0] > date[0]: 
            answer.append(i+1)
        elif today[0] == date[0] and today[1] > date[1]:
            answer.append(i+1)
        elif today[0] == date[0] and today[1] == date[1] and today[2] > date[2]:
            answer.append(i+1)
            
    return answer