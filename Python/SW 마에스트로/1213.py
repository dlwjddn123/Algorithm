name = list(input())
temp = ["" for _ in range(len(name))]
N = len(name) // 2
name.sort()
count = [name.count(n) for n in name]
print(count)
# for i in range(N):
#     if i 
