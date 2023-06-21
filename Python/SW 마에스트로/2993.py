S = input()

def ReverseString(s):
    s_length = len(s)
    middleIdx = s_length // 2
    
    s = list(s)
    for i in range(middleIdx):
        temp = s[i]
        s[i] = s[s_length -1 - i]
        s[s_length -1 - i] = temp
    return "".join(s)

def SplitString(s):
    s_length = len(s)
    allCase = []
    for i in range(s_length-2):
        for j in range(i+1, s_length-1):
            allCase.append([s[:i+1], s[i+1:j+1], s[j+1:]])
    return allCase

def go(s):
    result = ""
    All = []
    case = SplitString(s)
    for n in case:
        a = ReverseString(n[0])
        b = ReverseString(n[1])
        c = ReverseString(n[2])
        All.append(a+b+c)
    All.sort()
    return All[0]
print(go(S))