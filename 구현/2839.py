N = int(input()) # 유연하게 생각하기..
count = 0

while True:
    if N % 5 == 0: # N이 0이거나 N % 5 가 0이면 
        count += N//5 # 5로 나눈 몫을 더함
        print(count)
        break
    N = N-3 # N이 0이 아니고 5로도 안나눠지면 3을 빼고 다시 실행
    count += 1 # 3KG 1개 담았으니 COUNT는 +1
    if N < 0 : # N이 음수가 되면 계산할 수 없는 수이므로 -1 출력
        print(-1)
        break


    