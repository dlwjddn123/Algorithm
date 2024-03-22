def solution(s):
    answer = ""
    numberMap = dict()
    numberMap["zero"] = "0"
    numberMap["one"], numberMap["two"], numberMap["three"] = "1", "2", "3"
    numberMap["four"], numberMap["five"], numberMap["six"] = "4", "5", "6"
    numberMap["seven"], numberMap["eight"], numberMap["nine"] = "7", "8", "9"

    temp = ""
    
    for i in range(len(s)):
        if s[i].isdigit():
            answer += s[i]
            continue
        temp += s[i]
        
        if numberMap.get(temp) != None:
            answer += numberMap[temp]
            temp = ""
        
    return int(answer)