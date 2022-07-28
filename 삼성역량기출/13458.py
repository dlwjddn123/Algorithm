N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())
count = 0
for n in A:
    if n - B <= 0 :
        count += 1
    else:
        count += 1
        if (n - B) % C == 0:
            count += (n-B) // C
        else:
            count += (n-B) // C + 1

print(count)