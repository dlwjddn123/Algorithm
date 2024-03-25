N = int(input())
S = input()
map = dict()

count, p1, p2 = 0, 0, 0
max_s = 1

while p2 < len(S):
    if count <= N:
        if map.get(S[p2]) == None or map.get(S[p2]) == 0:
            map[S[p2]] = 1
            if count == N and max_s < p2 - p1:
                max_s = p2 - p1
            count += 1
            p2 += 1
        else:
            map[S[p2]] += 1
            if max_s < p2 - p1 + 1:
                max_s = p2 - p1 + 1
            p2 += 1
            continue    

    if count > N:
        if map[S[p1]] > 1:
            map[S[p1]] -= 1
        else:
            map[S[p1]] = 0
            count -= 1
        p1 += 1

print(max_s)