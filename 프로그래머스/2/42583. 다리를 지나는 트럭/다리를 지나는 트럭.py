from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    truck_weights.reverse()
    bridge = deque([0 for _ in range(bridge_length)])
    currentWeight = 0
    
    while truck_weights:
        time += 1
        currentWeight -= bridge.popleft()
        
        if currentWeight + truck_weights[-1] <= weight:
            truck_weight = truck_weights.pop()
            currentWeight += truck_weight
            bridge.append(truck_weight)
        else:
            bridge.append(0)
            
    return time + bridge_length