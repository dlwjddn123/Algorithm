def solution(price, money, count):
    answer = money
    for i in range(count):
        answer -= price * (i + 1)
    
    if answer < 0:
        return -answer
    
    return 0