N, K = map(int, input().split())
Order = list(map(int, input().split()))
jobs = [[] for _ in range(K+1)]
process = []
context_switch_count = 0
for i in range(K):
    jobs[Order[i]].append(i)

for j in range(K):
    if Order[j] in process:
        jobs[Order[j]].pop(0)
        continue
    if len(process) < N:
        process.append(Order[j])
        jobs[Order[j]].pop(0)
    else:
        farthest = 0
        idx = 0
        chk = False
        for k in range(N):
            if len(jobs[process[k]]) == 0:
                process.pop(k)
                chk = True
                break
            else:
                if jobs[process[k]][0] > farthest:
                    farthest = jobs[process[k]][0]
                    idx = k
        if not chk:
            process.pop(idx)

        process.append(Order[j])
        jobs[Order[j]].pop(0)
        context_switch_count += 1

print(context_switch_count)
                    






