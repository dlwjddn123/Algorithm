def solution(key, lock):
    lockEmptySpace = set()
    for i in range(len(lock)):
        for j in range(len(lock)):
            if lock[i][j] == 0:
                lockEmptySpace.add((i, j))
    answer = find(key, lockEmptySpace, len(lock))
    return answer

def rotate(key):
    N = len(key)
    result = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            result[j][N - i - 1] = key[i][j]

    return result

def find(key, lockEmptySpace, M):
    N = len(key)
    for _ in range(4):
        key = rotate(key)
        newKey = copy(key)
        for i in range(N):
            if i != 0:
                newKey = up(newKey)
            if isMatched(newKey, lockEmptySpace, M):
                return True
            lKey = copy(newKey)
            for _ in range(N-1):
                lKey = left(lKey)
                if isMatched(lKey, lockEmptySpace, M):
                    return True
            rKey = copy(newKey)
            for _ in range(N-1):
                rKey = right(rKey)
                if isMatched(rKey, lockEmptySpace, M):
                    return True
                
        newKey = copy(key)
        for i in range(N):
            if i != 0:
                newKey = down(newKey)
            if isMatched(newKey, lockEmptySpace, M):
                return True
            lKey = copy(newKey)
            for _ in range(N-1):
                lKey = left(lKey)
                if isMatched(lKey, lockEmptySpace, M):
                    return True
            rKey = copy(newKey)
            for _ in range(N-1):
                rKey = right(rKey)
                if isMatched(rKey, lockEmptySpace, M):
                    return True
    return False

def copy(key):
    return [k[:] for k in key]

def up(key):
    key.remove(key[0])
    key.append([0 for _ in range(len(key) + 1)])
    return key
    
def down(key):
    key.insert(0, [0 for _ in range(len(key))])
    key.remove(key[-1])
    return key

def left(key):
    for i in range(len(key)):
        key[i].pop(0)
        key[i].append(0)
    return key

def right(key):
    for i in range(len(key)):
        key[i].insert(0, 0)
        key[i].pop()
    return key

def isMatched(key, lockEmptySpace, N):
    result = []
    keyPlace = set()
    for i in range(len(key)):
        for j in range(len(key)):
            if key[i][j] == 1:
                keyPlace.add((i, j))
    result.append(keyPlace)
    
    for k in range(N - len(key) + 1):
        for h in range(N - len(key) + 1):
            temp = set()
            for i, j in keyPlace:
                temp.add((i+k, j+h))
            result.append(temp)
            
    return lockEmptySpace in result
