S = list(input())
stack = []
total = 0

if len(S) == 2:
    if S[0] == '(' and S[1] == ')':
        print(2)
    elif S[0] == '[' and S[1] == ']':
        print(3)
    else:
        print(0)        
else:
    for i in range(len(S)):
        if S[i] == "(":
            stack.append(["(", 0])
        elif S[i] == ")":
            if len(stack) == 0 or stack[-1][0] != "(":
                stack.append(-1)
                break 
            s, n = stack.pop()
            if s == '(':
                if len(stack) == 0:
                    if n == 0:
                        total += 2
                        continue
                    total += n * 2
                else:
                    if n == 0:
                        stack[-1][1] += 2
                    else:
                        stack[-1][1] += n * 2

        elif S[i] == "[":
            stack.append(["[", 0])
        elif S[i] == "]":
            if len(stack) == 0 or stack[-1][0] != "[":
                stack.append(-1)
                break 
            s, n = stack.pop()
            if s == '[':
                if len(stack) == 0:
                    if n == 0:
                        total += 3
                        continue
                    total += n * 3
                else:
                    if n == 0:
                        stack[-1][1] += 3
                    else:
                        stack[-1][1] += n * 3

    if len(stack) == 0:
        print(total)
    else:
        print(0)  