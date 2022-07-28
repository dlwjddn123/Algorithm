from collections import deque
N = int(input())
top = list(map(int, input().split()))
stack = [0]
result = [0]
for i in range(1, N):
    if top[stack[0]] < top[i] :
        stack = [i]
        result.append(0)
        continue
    if top[i] < top[stack[-1]] :
        result.append(stack[-1]+1)
        stack.append(i)
    else:  
        while True:
            stack.pop()
            if top[i] < top[stack[-1]]:
                result.append(stack[-1]+1)
                stack.append(i)
                break

print(*result)


     



