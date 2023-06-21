from collections import deque

cryptogram = input()
N = int(input())
words = [input() for _ in range(N)]
key = deque()

for i in range(97, 123):
    key.append(chr(i))

def go():
    for i in range(26):
        if i != 0:
            key.rotate(1)
        temp = ""
        for c in cryptogram:
            temp += key[ord(c) - 97]
        
        for w in words:
            if w in temp:
                print(temp)
                return
go()