def solution(data, ext, val_ext, sort_by):
    answer = []
    
    dataMap = dict()
    dataMap["code"] = 0
    dataMap["date"] = 1
    dataMap["maximum"] = 2
    dataMap["remain"] = 3
    
    idx = dataMap[ext]
    
    for i in range(len(data)):
        if data[i][idx] < val_ext:
            answer.append(data[i])
    
    key = dataMap[sort_by]
    answer.sort(key=lambda x : x[key])
    return answer