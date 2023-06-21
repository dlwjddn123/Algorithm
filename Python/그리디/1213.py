S = list(input())
S.sort()
result = ['' for _ in range(len(S))]
idx = 0
i = 0
while len(S) >= 2:
    if S[idx] == S[idx+1]:      
        result[i] = S.pop(idx)
        result[-i-1] = S.pop(idx)
        i += 1
    else:
        idx += 1

    if idx >= len(S)-1:
        break
if len(S) == 1:
    result[i] = S.pop()
    print(''.join(result))
elif len(S) == 0:
    print(''.join(result))
else:
    print("I'm Sorry Hansoo")