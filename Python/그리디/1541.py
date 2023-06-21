T = input()
arr = []
temp = ""
result = 0
for i in range(len(T)):
    if T[i] == "-":
        arr.append(int(temp))
        arr.append("-")
        temp = ""
    elif T[i] == "+":
        arr.append(int(temp))
        arr.append("+")
        temp = ""
    else:
        temp += T[i]
    if i == len(T)-1:
        arr.append(int(temp))
        
j = 0
temp = 0
check = False
while len(arr)> j:
    if check and (arr[j] != "-" and arr[j] != "+"):
        temp += arr[j]
        j += 1
        continue
    if arr[j] == "-":
        check = True
    elif arr[j] == "+":
        if check:
            pass
        else:
            check = False
    else:
        result += arr[j]
    j += 1

print(result-temp)
