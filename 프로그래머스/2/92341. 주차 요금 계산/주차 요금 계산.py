import math

def solution(fees, records):
    answer = []
    park = [["", False, 0] for _ in range(10000)]
    carNumbers = []
    for record in records:
        time, carNumber, type = record[:5], int(record[6:10]), record[11:]
        if type == "IN":
            park[carNumber][0] = time
            park[carNumber][1] = True
            if carNumber not in carNumbers:
                carNumbers.append(carNumber)
        elif type == "OUT":
            park[carNumber][1] = False
            inHour, inMinute = int(park[carNumber][0][:2]), int(park[carNumber][0][3:])
            outHour, outMinute = int(time[:2]), int(time[3:])
            totalTime = (outHour * 60 + outMinute) - (inHour * 60 + inMinute)
            park[carNumber][2] += totalTime
    
    carNumbers.sort()
    
    for carNumber in carNumbers:
        if park[carNumber][1]:
            inHour, inMinute = int(park[carNumber][0][:2]), int(park[carNumber][0][3:])
            outHour, outMinute = 23, 59
            totalTime = (outHour * 60 + outMinute) - (inHour * 60 + inMinute)
            park[carNumber][2] += totalTime
            
        totalPrice = fees[1]
        if park[carNumber][2] > fees[0]:
            totalPrice += math.ceil((park[carNumber][2] - fees[0]) / fees[2]) * fees[3] 
        answer.append(totalPrice)
    
    return answer