def solution(players, callings):
    answer = []
    hashMap = dict()
    for i in range(len(players)):
        hashMap[players[i]] = i
        
    for calling in callings:
        idx = hashMap[calling]
        hashMap[calling] -= 1
        temp = players[idx-1]
        hashMap[temp] += 1
        players[idx-1] = players[idx]
        players[idx] = temp
    
    return players