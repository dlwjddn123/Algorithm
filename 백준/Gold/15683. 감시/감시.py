from collections import deque

N, M = map(int, input().split())
office = []
cctvPositions = []
blindSpots = []
for y in range(N):
    row = list(map(int, input().split()))
    for x in range(M):
        if row[x] != 0 and row[x] != 6:
            cctvPositions.append([y, x])
    office.append(row)

left, right, up, down = [0, -1], [0, 1], [-1, 0], [1, 0]
CCTV1 = [[left], [right], [up], [down]]
CCTV2 = [[left, right], [up, down]]
CCTV3 = [[left, up], [left, down], [right, up], [right, down]]
CCTV4 = [[left, up, right], [left, down, right], [left, up, down], [right, up, down]]
CCTV5 = [[left, right, up, down]]

cctvDirects = {1: CCTV1, 2: CCTV2, 3: CCTV3, 4: CCTV4, 5: CCTV5}

def countBlindSpot(checkedOffice):
    count = 0
    for i in range(N):
        for j in range(M):
            if checkedOffice[i][j] == 0:
                count += 1
    return count

def markMonitoredSpot(direct, office, pos):
    q = deque()
    q.append(pos)
    while q:
        spot = q.popleft()
        ny = spot[0] + direct[0]
        nx = spot[1] + direct[1]
        if 0 <= ny < N and 0 <= nx < M and office[ny][nx] != 6:
            if office[ny][nx] not in [1,2,3,4,5]:
                office[ny][nx] = '#'
            q.append([ny, nx])

def find_min_blind_spot(idx, office):
    if idx == len(cctvPositions):
        blindSpots.append(countBlindSpot(office))
        return
    cctvPos = cctvPositions[idx]
    cctvNum = office[cctvPos[0]][cctvPos[1]]
    directs = cctvDirects.get(cctvNum)
    for direct in directs:
        copyOffice = [office[i][::] for i in range(N)]
        for dir in direct:
            markMonitoredSpot(dir, copyOffice, cctvPos)
        find_min_blind_spot(idx + 1, copyOffice)


find_min_blind_spot(0, office)
print(min(blindSpots))


