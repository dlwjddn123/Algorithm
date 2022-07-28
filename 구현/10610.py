N = input() # 너무 어렵게 생각해서 오래 걸린 문제
arr = list(map(int,N))
Sum = sum(arr)

if Sum % 3 == 0:
    arr.sort(reverse=True) # 내림차순하고 그냥 30으로만 나눠지면 됨..
    l = arr[-1] # 예시를 정확히 들고 푸는 습관을 들이자
    if l == 0:
        a = ''.join(map(str,arr))
        a = int(a)
        print(a)
    else:
        print(-1)
else:
    print(-1)