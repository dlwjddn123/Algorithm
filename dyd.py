def combination(n, r):
    result = []
    temp = []
    def dfs(current):
        if len(temp) == r:
            result.append(temp[::])
            return
        for i in range(current, len(n)):
            temp.append(n[i])
            dfs(i+1)
            temp.pop()
    dfs(0)
    return result

a = [1,2,3,4,5,6,7,8,9]
s = combination(a, 3)
for n in s:
    print(n)



