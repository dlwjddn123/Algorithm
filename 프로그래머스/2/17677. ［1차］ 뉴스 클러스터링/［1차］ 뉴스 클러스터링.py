def solution(str1, str2):
    answer = 0
    str1 = str1.lower()
    str2 = str2.lower()
    str1Map = getVaildStringPairMap(str1)
    str2Map = getVaildStringPairMap(str2)
    
    answer = getJaccard(str1Map, str2Map) * 65536
    return int(answer)

def getVaildStringPairMap(string):
    result = dict()
    for i in range(len(string) - 1):
        if string[i].isalpha() and string[i + 1].isalpha():
            temp = string[i] + string[i + 1]
            if result.get(temp) == None:
                result[temp] = 1
            else:
                result[temp] += 1
    return result
        
def getJaccard(map1, map2):
    count = 0
    union = 0
    for key in map1.keys():
        if map2.get(key) != None:
            count += min(map1[key], map2[key])
            union += max(map1[key], map2[key])
            continue
        union += map1[key]
        
    for key in map2.keys():
        if map1.get(key) == None:
            union += map2[key]
    
    if count == 0 and union == 0:
        return 1
    
    return count / union