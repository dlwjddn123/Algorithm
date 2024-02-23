diaFatigue = {"diamond" : 1, "iron" : 1, "stone" : 1}
ironFatigue = {"diamond" : 5, "iron" : 1, "stone" : 1}
stoneFatigue = {"diamond" : 25, "iron" : 5, "stone" : 1}

def solution(picks, minerals):
    answer = 0
    minerals = [minerals[i:i+5] for i in range(0, len(minerals), 5)[:sum(picks)]]
    minerals.sort(key = lambda x : (-x.count("diamond"), -x.count("iron"), -x.count("stone")))
    
    for mineral in minerals:
        if picks[0] > 0:
            for i in range(len(mineral)):
                answer += diaFatigue[mineral[i]]
            picks[0] -= 1
            continue
        if picks[1] > 0:
            for i in range(len(mineral)):
                answer += ironFatigue[mineral[i]]
            picks[1] -= 1
            continue
        if picks[2] > 0:
            for i in range(len(mineral)):
                answer += stoneFatigue[mineral[i]]
            picks[2] -= 1
                
    return answer