import sys
input = sys.stdin.readline
S = list(input().rstrip())

result = ""
tagChk = False
temp = []
for n in S:
    if n == ">":
        tagChk = False
        result += n
        continue
    if tagChk:
        result += n
        continue
    if n == "<":
        if temp:
            while temp:
                result += temp.pop()
        tagChk = True
        result += n
        continue
    if n == " ":
        while temp:
            result += temp.pop()
        result += " "
        continue
    temp.append(n)
while temp:
    result += temp.pop()

print(result)