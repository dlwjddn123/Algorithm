S = list(input())
count = 0
def permutations(arr, r):
    arr.sort()
    used = [0 for _ in range(len(arr))]
    result = []
    
    def generate(chosen, used):
        if len(chosen) == r:
            result.append(''.join(chosen[:]))
            return
        
        for i in range(len(arr)):
            if not used[i] and (i == 0 or arr[i-1] != arr[i] or used[i-1]):
                chosen.append(arr[i])
                used[i] = 1
                generate(chosen, used)
                used[i] = 0
                chosen.pop()
    generate([], used)
    return result

def find(s):
    for i in range(1, len(s)-1):
        if s[i-1] != s[i] and s[i] != s[i+1]:
            continue
        else:
            return 0
    return 1

result = permutations(S, len(S))
for n in result:
    if find(n):
        count += 1
        continue

print(count)