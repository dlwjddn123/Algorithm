N = int(input()) #중간 기점으로 반복문 두 번 돌렸음
gap = " "
for i in range(N):
    print(gap*i,end='')
    n = 2*(N-i)-1
    for _ in range(n):
        print("*", end='')
    print()
# 중간
for j in range(N-1,0,-1):
    print(gap*(j-1),end='')
    n = 2*(N-j)+1
    for w in range(n):
        print("*",end='')
    print()

