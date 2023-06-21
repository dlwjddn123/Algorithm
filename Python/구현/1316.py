N = int(input()) # True False를 0 1로 쓰지 않기
count = 0
for _ in range(N):
    word = input()
    dup = set()
    check = True
    for i in range(len(word)):
        if word[i] not in dup: # word[i]가 dup에 겹치는 것이 있는지 확인
            dup.append(word[i]) # 없으면 dup에 추가
        elif word[i] == word[i-1]: # 같은 문자가 연속으로 나오면
            continue # 틀린것이 아니므로 그냥 넘김
        else: # 이외에 겹치는 것이 있으면
            check = False 
            break
    if check == True: 
        count += 1
print(count)
    



    
