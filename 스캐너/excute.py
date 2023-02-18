from .scanner import MiniScanner

sc = MiniScanner("test.txt")
while(sc.idx < len(sc.src)):
    tok = sc.getToken()
    print(tok)