N = int(input())

MAX = [0] * N
MIN = [0] * N

for _ in range(N):
    a, b, c = map(int, input().split())
    t0 = max(MAX[0], MAX[1])
    t2 = max(MAX[1], MAX[2])
    MAX[0] = a + t0
    MAX[1] = b + max(t0, t2)
    MAX[2] = c + t2
    
    t0 = min(MIN[0], MIN[1])
    t2 = min(MIN[1], MIN[2])
    MIN[0] = a + t0
    MIN[1] = b + min(t0, t2)
    MIN[2] = c + t2

    print(MAX)
    
print(max(MAX), min(MIN))