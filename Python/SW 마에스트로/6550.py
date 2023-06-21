while True:
    try :
        s, t = input().split()
        count = 0
        k = 0
        for i in range(len(s)):
            while k <= len(t) - 1:
                if s[i] == t[k] :
                    k += 1
                    count += 1
                    break
                k += 1

        if count == len(s): 
            print("Yes")
        else:
            print("No")
    except :
        break