def solution(storey):
    answer = 0
    btn = [10**i for i in range(9)]
    count = 0
    if storey == btn[0]:
        return 1
    
    for i in range(len(btn)-1):
        print(storey, count)
        if storey < btn[i]:
            break
        if storey % btn[i+1] // btn[i] < 5:
            cnt = storey % btn[i+1] // btn[i]
            storey -= btn[i] * cnt
            count += cnt
        elif storey % btn[i+1] // btn[i] == 5:
            if storey % (btn[i+1]*10) // btn[i+1] >= 5:
                storey += btn[i] * 5
            else:
                storey -= btn[i] * 5
            count += 5
        else:
            cnt = (btn[i+1] - storey % btn[i+1]) // btn[i]
            storey += btn[i] * cnt
            count += cnt
            
    for i in range(len(btn)):
        if storey >= btn[-i-1]:
            cnt = storey // btn[-i-1]
            storey -= btn[-i-1] * cnt
            count += cnt
    return count