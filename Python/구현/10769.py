import sys # 입출력 문제는 sys 쓰기

input = sys.stdin.readline

S = list(input().split(":"))
happy = 0
sad = 0
for i in S:
    if "-)" in i:
        happy += 1
    elif "-(" in i:
        sad += 1
if happy - sad > 0 :
    print("happy")
elif happy - sad < 0:
    print("sad")
elif happy - sad == 0 and happy >= 1:
    print("unsure")
else:
    print("none")
