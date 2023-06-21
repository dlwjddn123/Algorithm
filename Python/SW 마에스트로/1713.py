N = int(input())
vote = int(input())
voteList = list(map(int, input().split()))
candidates = []
students = [[0, i] for i in range(101)]
nums = []
for i in range(len(voteList)):
    if voteList[i] not in nums:
        if len(candidates) < N:
            students[voteList[i]][0] += 1
            candidates.append(students[voteList[i]])
            nums.append(voteList[i])
            continue
        Min = min(list(c[0] for c in candidates))
        for j in range(N):
            if candidates[j][0] == Min:
                idx = candidates.pop(j)
                students[idx[1]][0] = 0
                students[voteList[i]][0] += 1
                candidates.append(students[voteList[i]])
                nums.pop(j)
                nums.append(voteList[i])
                break
    else:
        students[voteList[i]][0] += 1
nums.sort()
print(*nums)

