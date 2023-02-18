import sys
input = sys.stdin.readline

N = int(input())
sides = [int(input()) for _ in range(N)]
sides.sort(reverse = True)
def go():
    for i in range(N-2):
        if sides[i] < sides[i+1] + sides[i+2]:
            print(sides[i] + sides[i+1] + sides[i+2])
            return
    print(-1)

go()