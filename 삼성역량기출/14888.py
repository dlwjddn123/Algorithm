from re import M


N = int(input())
numbers = list(map(int, input().split()))
A = list(map(int, input().split()))
op = []
Max = -1000000000
Min = 1000000000
for i in range(4):
    if i == 0:
        n = ["+" for _ in range(A[i])]
        op += n
    elif i == 1:
        n = ["-" for _ in range(A[i])]
        op += n
    elif i == 2:
        n = ["*" for _ in range(A[i])]
        op += n
    elif i == 3:
        n = ["/" for _ in range(A[i])]
        op += n

def bt(cur, oper):
    global op, Max, Min, numbers
    numbers1 = numbers[::]
    if len(oper) == 0:
        total = 0
        for i in range(N-1):
            if cur[i] == "+":
                numbers1[i+1] = numbers1[i] + numbers1[i+1]
            elif cur[i] == "-":
                numbers1[i+1] = numbers1[i] - numbers1[i+1]
            elif cur[i] == "*":
                numbers1[i+1] = numbers1[i] * numbers1[i+1]
            elif cur[i] == "/":
                if numbers1[i+1] == 0:
                    return
                if numbers1[i] < 0:
                    numbers1[i+1] = -(-numbers1[i] // numbers1[i+1])    
                else:
                    numbers1[i+1] = numbers1[i] // numbers1[i+1]
        total = numbers1[-1]
        if total > Max:
            Max = total
        if total < Min:
            Min = total
        return

    for n in oper:
        temp = cur[::]
        temp2 = oper[::]
        temp += n
        temp2.remove(n)
        bt(temp, temp2)

bt([], op)   
print(Max)
print(Min)