def solution(id_list, report, k):
    answer = []
    mailCount = dict()
    reports = dict()
    for id in id_list:
        reports[id] = set()
        mailCount[id] = 0
        
    for n in report:
        id1, id2 = n.split()
        reports[id2].add(id1)
    
    for key in reports.keys():
        if len(reports[key]) >= k:
            for target in reports[key]:
                mailCount[target] += 1
    
    for id in id_list:
        answer.append(mailCount[id])
    return answer