from enum import Enum, auto

class MiniScanner:
    src =""
    idx = 0
    error_msg = ""
    def __init__(self, PATH):
        self.src = self.parseFile(PATH)

    class State(Enum): # 현재 상태를 나타내는 열거형 상수
        Initial = auto() # 초기 상태 
        Dec = auto() # 10진법 숫자
        Oct = auto() # 8진법 숫자
        Hex = auto() # 16진법 숫자
        Float = auto() # 실수
        IdOrKeyword = auto() # 식별자 혹은 키워드
        Operator = auto() # 연산자
        Zero = auto() # 8진법과 16진법을 식별하기 위해 0으로 시작하는 상태
        PreHex = auto() # 0x인 상태
        PreFloat = auto() # 실수로 갈 수 있는 상태중 10.3e+ 까지의 상태, 즉 이 상태로 끝나면 에러
        Dot = auto() # 실수를 표현하기 위한 상태로 10. 까지의 상태, 이 상태로 끝나면 에러
        Exponential = auto() # 실수를 표현하기 위한 상태로 10.3e 까지의 상태
        SingleOperator = auto() # 연산자 하나 그 자체로 사용될 수 있는 연산자 모음 상태
        Literal = auto() # 리터럴 상수를 표현하기 위한 상태
        Comment = auto() # 주석문 상태
        IdError = auto() # 식별자가 숫자로 시작했을 때를 처리하는 상태

    def parseFile(self, PATH): # 파일을 읽어와 문자열로 저장 후 리턴하는 메서드
        try:
            p = open(PATH, "rt", encoding = 'UTF8') # 파일을 읽어오는 함수
            LIST = p.readlines()
            string = "".join(LIST).replace("\n", " ")
            if len(string) == 0:
                self.error_msg = "ERROR : 읽어올 텍스트가 없습니다"
                return
        except:
            self.error_msg = "ERROR : 파일을 읽어올 수 없습니다"
            return
        string = "".join(map(str, string))
        return string

    def getToken(self): # string을 읽어와 분석 후 토큰 식별
        token = Token()
        symType = Token.SymbolType.Null
        tokenValue = "" # 토큰의 원시값
        self.error_msg = "" # 에러가 났을 떄 내용을 담을 변수
        state = self.State.Initial # 초기 상태
        while (self.idx < len(self.src)): # idx가 string의 끝을 가르킬때까지 계속 실행
            c = self.src[self.idx]
            self.idx += 1
            if (c == "/" and self.src[self.idx] == "*"): # 주석을 제거하는 알고리즘 /와 *을 연속으로 만났을 때,
                state = self.State.Comment # 상태를 주석 상태로 바꾸고 idx를 1더하고 다음 반복문으로
                self.idx += 1
                continue
            elif (state == self.State.Comment): # 상태가 주석 상태일 때,
                if (self.idx == len(self.src)):
                    self.error_msg = "ERROR : 주석이 정상적으로 종료되지 않았습니다"
                    break
                if (c == "*" and self.src[self.idx] == "/"): # */가 연속으로 나올 때, 상태를 초기 상태로 바꾸고 idx +1 한 후 continue
                    self.idx += 1
                    state = self.State.Initial 
                    continue
                else:
                    continue
            elif (c != "'" and state == self.State.Literal and not c.isdigit() and not c.isalpha()):
                # 상수를 걸러내기 위한 조건으로, 상태가 Literal인데 연산자나 특수기호가 나오면 에러를 출력
                self.error_msg = "ERROR : 상수가 정상적으로 끝나지 않았음"
                self.idx -=1
                break
            elif (c == " " ): # 초기 상태가 아닌 상태에서 공백 문자를 읽으면 반복문을 끝내서 토큰을 짜름
                if (state != self.State.Initial):
                    break
                else: # 초기 상태에서 공백 문자를 읽으면 단순히 다음 반복문으로 넘김
                    continue

            elif (self.isSingleSpecialToken(c)): # 연산자 하나 자체로 쓰일 수 있는 연산자를 만났을 때
                if (state == self.State.Initial): # 초기 상태라면 상태를 SingleOperator로 바꾸고 break
                    state = self.State.SingleOperator
                    tokenValue += c
                else: # 초기 상태가 아니라면 종료하여 그 전 상태에 있던 토큰을 짜르고 반복문을 다시 시작
                    self.idx -= 1
                break

            elif (self.isSpecialToken(c)): # 특수 기호를 만났을 때,
                if (c == '.' and state == self.State.Dec): # .을 읽었는데 상태가 10진법을 가르키는 Dec라면,
                    state = self.State.Dot # 실수를 표현하기 위한 . 이므로 상태를 Dot로 변경
                    tokenValue += c
                    continue
                elif (c == "+" and state == self.State.Exponential): # +를 만났는데 상태가 실수를 가르키기 위한 Exponential일 때,
                    state = self.State.PreFloat # 실수를 표현하기 위한 상태로 변경하고, 다음 문자가 숫자가 오면 정상종료, 아니면 에러
                    tokenValue += c
                    continue
                elif (c == "-" and state == self.State.Exponential): # 위의 +와 같음
                    state = self.State.PreFloat
                    tokenValue += c
                    continue
                elif (c == "'" ): # 리터럴을 표현하기 위한 기호로 '를 만났을 때,
                    if (state == self.State.Initial): # 초기 상태라면 리터럴을 표현하기 위한 상태로 변경
                        state = self.State.Literal
                        tokenValue += c
                        continue
                    elif (state == self.State.Literal): # 상태가 Literal이면 리터럴을 종료하기 위한 기호로 상태를 종료하여 토큰을 짜름
                        tokenValue += c
                    else: # 초기 상태와 Literal 상태가 둘 다 아니라면, 이 전의 상태를 종료하면서 토큰을 짜르고 다시 반복문 시작
                        self.idx -= 1
                    break
                elif (state != self.State.Initial and state != self.State.Operator): # 초기 상태도 아니고 Operator도 아니라면 상태를 종료
                    self.idx -= 1
                    break
                state = self.State.Operator # 모든 조건에서 continue나 break를 만나지 않은 경우는 상태를 Operator로 변경
 
            elif (state == self.State.Initial and c == "0"): # 초기 상태이고 0을 만나면 Zero상태로 변경
                state = self.State.Zero

            elif (c.isdigit()): # 숫자일 때,
                if (state == self.State.Initial): # 초기 상태면 10진법 상태로 변경
                    state = self.State.Dec
                elif (state == self.State.Dec): # 10진법 상태면 pass
                    pass
                elif (state == self.State.Zero): # Zero상태에서 숫자를 만나면 8진법 상태로 변경
                    state = self.State.Oct
                elif (state == self.State.PreHex): # preHex상태에서 숫자를 만나면 16진법 상태로 변경
                    state = self.State.Hex
                elif (state == self.State.Dot):# Dot상태에서 숫자를 만나면 실수 상태로 변경
                    state = self.State.Float
                elif (state == self.State.Exponential): # Exponential상태에서 숫자를 만나면 실수 상태로 변경
                    state = self.State.Float
                elif (state == self.State.PreFloat): # PreFloat상태에서 숫자를 만나면 실수 상태로 변경
                    state = self.State.Float
                elif (state == self.State.Float): # 실수 상태에서 숫자를 만나면 pass
                    tokenValue += c
                    continue
                elif (state == self.State.IdOrKeyword): # 식별자 키워드 상태이면 pass
                    tokenValue += c
                    continue
                elif (state == self.State.Literal): # 리터럴 상태이면 pass
                    tokenValue += c
                    continue
                elif (state == self.State.IdError): # 식별자 오류인 상태면
                    tokenValue += c
                    continue
                else: # 모든 조건에서 걸리지 않는다면 상태를 종료
                    self.idx -= 1
                    break

            elif(c.isalpha() or c == "_"): # 알파벳이나 _를 읽었을 때,
                if (c == "e" and (state == self.State.Dec or state == self.State.Dot or state == self.State.Float)): # e이고 실수를 가르키기 위한 상태 중 하나일 때, Exponential로 상태 변경
                    state = self.State.Exponential
                    tokenValue += c
                    continue
                elif (c == "x" and state == self.State.Zero): # 상태가 Zero이고 x를 만나면 16진법을 위한 상태인 PreHex로 변경
                    state = self.State.PreHex
                    tokenValue += c
                    continue
                elif ((state == self.State.PreHex or state == self.State.Hex) and (c == "A" or c == "B" or c == "C" or c == "D" or c == "E" or c == "F"\
                    or "a" or c == "b" or c == "c" or c == "d" or c == "e" or c == "f")): # 상태가 PreHex 또는 Hex이면서 a~f까지의 알파벳을 만났을 때, 16진법 처리
                    state = self.State.Hex
                    tokenValue += c
                    continue
                elif (state == self.State.Literal): # 리터럴이면 토큰에 값을 추가하고 continue
                    tokenValue += c
                    continue
                elif (state == self.State.Zero or state == self.State.Dec or state == self.State.Float or state == self.State.PreHex or \
                    state == self.State.PreFloat or state == self.State.Dot or state == self.State.Hex or state == self.State.Oct): 
                    # 숫자 이후 공백 없이 알파벳 문자가 나온 경우, 식별자 오류이기 때문에 식별자 오류 상태로 변환
                    state = self.State.IdError
                    self.error_msg = "ERROR : 식별자 이름이 잘못되었습니다"
                    tokenValue += c
                    continue
                elif (state == self.State.IdError):
                    tokenValue += c
                    continue
                elif (state != self.State.IdOrKeyword and state != self.State.Initial): # 식별자 키워드 상태도 아니고 초기 상태도 아니라면 상태를 종료
                    self.idx -= 1
                    break
                
                state = self.State.IdOrKeyword # 모든 조건에서 continue나 break에 걸리지 않으면 식별자 키워드 상태
            tokenValue += c # 반복문이 시작하고서 모든 조건에서 continue나 break에 걸리지 않으면 토큰 원시값에 c를 더하고 다음 반복문 시작
        symType = self.getSymbolType(state.name) # 위의 모든 상태들을 대분류 시키는 함수
        token.setSymbol(tokenValue, symType, self.error_msg) # 대분류된 상태에서 정확한 토큰 번호를 매칭 시켜주는 함수 + 토큰 원시값 + 에러 문자 전달
        return token # 생성된 토큰을 반환

    def isSingleSpecialToken(self, c): # 연산자 하나 자체로 쓰이는 기호를 식별하는 메서드
        if (c == "(" or c == ")" or c == "[" or c == "]" or c == "{" or\
            c == "}" or c == ";" or c == ","):
            return True
        else:
            return False

    def isSpecialToken(self, c): # 다른 연산자와 같이 사용될 수 있는 기호를 식별하는 메서드
        if (c == "!" or c == "=" or c == "+" or c == "-" or c == "/" or \
            c == "*" or c == "&" or c == "|" or c == "<" or c == ">" or c == '.' or c == "'"):
            return True
        else:
            return False
    
    def getSymbolType(self, s): # 현재 상태를 통해 Token의 대분류에 속하는 타입으로 변환
        if (s == "Dec" or s == "Hex" or s == "Oct" or s == "Zero" or s == "Float" or s == "Exponential"):
            return Token.SymbolType.Digit
        elif (s == "IdOrKeyword"):
            return Token.SymbolType.IdOrKeyword
        elif (s == "Operator" or s == "SingleOperator"):
            return Token.SymbolType.Operator
        elif (s == "Literal"):
            return Token.SymbolType.Literal
        else:
            return Token.SymbolType.Null
idNumber = 0
class Token:
    global idNumber # 토큰 번호
    tokenValue = "" # 토큰의 원시 값 
    symbol = None
    error_msg = ""

    def __init__(self):
        self.symbol = self.TokenSymbol.tNULL
        self.tokenValue = ""
    
    def __str__(self):
        if self.error_msg: # 에러가 있으면 에러 문구와 같이 출력
            return self.tokenValue + "\t : (" + str(self.symbol.value) + ", " + str(0) + ")" + " => " + self.error_msg
        elif self.symbol.name == "tId": # 식별자이면 몇 번째 식별자인지에 대한 번호를 출력
            return self.tokenValue + "\t : (" + str(self.symbol.value) + ", " + str(idNumber) + ")"
        else: # 나머지는 0으로 출력
            return self.tokenValue + "\t : (" + str(self.symbol.value) + ", " + str(0) + ")"

    class SymbolType(Enum): # 대분류 => 연산자, ID혹은 예약어, 숫자, NULL, 리터럴 상수
        Operator = auto()
        IdOrKeyword = auto()
        Digit= auto(), 
        Null = auto()
        Literal = auto()

    class TokenSymbol(Enum): # 소분류 
        tNULL = -1
        tId = 3
        tLiteral = 4
        tInteger = 5
        tReal = 6
        tPlus = 10
        tMinus = 11
        tMul = 12
        tDiv = 13
        tMod = 14 
        tAssign = 15 
        tNot = 16
        tAnd = 17
        tOr = 18 
        tEqual = 19
        tNotEq = 20
        tLess = 21
        tGreat= 22
        tLesser = 23
        tGreater = 24 
        tPlusAssign = 25
        tMinusAssign = 26
        tMulAssign = 27
        tDivAssign = 28
        tModAssign = 29 
        tLBracket = 30
        tRBracket = 31
        tLBrace = 32
        tRBrace = 33
        tLParen = 34
        tRParen = 35
        tComma = 36
        tSemicolon = 37
        tLQuotes = 38
        tRQuotes = 39 
        tIf = 40
        tWhile = 41
        tFor = 42
        tConst = 43
        tInt = 44
        tFloat = 45
        tElse = 46
        tReturn = 47
        tVoid = 48
        tBreak = 49
        tContinue = 50
        tChar = 51
        tDot = 52
    
    def getIdOrKeywordSymbol(self, token): # 입력받은 토큰이 문자열일때, 키워드인지 Id인지 구분하는 메서드
    
        if token == "const": return Token.TokenSymbol.tConst
        elif token == "else": return Token.TokenSymbol.tElse
        elif token == "if": return Token.TokenSymbol.tIf
        elif token == "int": return Token.TokenSymbol.tInt
        elif token == "float": return Token.TokenSymbol.tFloat
        elif token == "return": return Token.TokenSymbol.tReturn
        elif token == "void": return Token.TokenSymbol.tVoid
        elif token == "while": return Token.TokenSymbol.tWhile
        elif token == "for": return Token.TokenSymbol.tFor
        elif token == "break": return Token.TokenSymbol.tBreak
        elif token == "char": return Token.TokenSymbol.tChar
        elif token == "continue": return Token.TokenSymbol.tContinue
        else: # 위에 키워드들에 속하지 않으면, Id로 판단
            return Token.TokenSymbol.tId
            
    def getOperatorSymbol(self, token): # 입력받은 토큰이 연산자일때, 연산자를 구분해주는 메서드
        if token == "!": return Token.TokenSymbol.tNot
        elif token == "!=": return Token.TokenSymbol.tNotEq
        elif token == "%": return Token.TokenSymbol.tMod
        elif token == "%=": return Token.TokenSymbol.tModAssign
        elif token == "+": return Token.TokenSymbol.tPlus
        elif token == "+=": return Token.TokenSymbol.tPlusAssign
        elif token == "-": return Token.TokenSymbol.tMinus
        elif token == "-=": return Token.TokenSymbol.tMinusAssign
        elif token == "=": return Token.TokenSymbol.tAssign
        elif token == "==": return Token.TokenSymbol.tEqual
        elif token == "<": return Token.TokenSymbol.tLess
        elif token == "<=": return Token.TokenSymbol.tLesser
        elif token == ">": return Token.TokenSymbol.tGreat
        elif token == ">=": return Token.TokenSymbol.tGreater
        elif token == "*": return Token.TokenSymbol.tMul
        elif token == "*=": return Token.TokenSymbol.tMulAssign
        elif token == "/": return Token.TokenSymbol.tDiv
        elif token == "/=": return Token.TokenSymbol.tDivAssign
        elif token == "[": return Token.TokenSymbol.tLBracket
        elif token == "]": return Token.TokenSymbol.tRBracket
        elif token == "{": return Token.TokenSymbol.tLBrace
        elif token == "}": return Token.TokenSymbol.tRBrace
        elif token == "(": return Token.TokenSymbol.tLQuotes
        elif token == ")": return Token.TokenSymbol.tRQuotes
        elif token == "&&": return Token.TokenSymbol.tAnd
        elif token == "||": return Token.TokenSymbol.tOr
        elif token == '.' : return Token.TokenSymbol.tDot
        elif token == ",": return Token.TokenSymbol.tComma
        elif token == ";": return Token.TokenSymbol.tSemicolon
        elif token == "&" or token == "|":
             self.error_msg = "ERROR : 인식하지 못하는 기호 입니다"
             return Token.TokenSymbol.tNULL
        else:
             self.error_msg = "ERROR : 인식하지 못하는 기호 입니다"
             return Token.TokenSymbol.tNULL

    def setSymbol(self, token, type, err):
        global idNumber
        self.tokenValue = token
        self.error_msg = err
        if type == Token.SymbolType.IdOrKeyword:
            self.symbol = self.getIdOrKeywordSymbol(token)
            if (self.symbol == Token.TokenSymbol.tId): # Id일 경우
                idNumber += 1 # id의 순서값을 나타내는 idNumber에 +1
        elif type == Token.SymbolType.Digit:
            try:    
                if isinstance(int(token), int): # 정수형이면
                    self.symbol = Token.TokenSymbol.tInteger
            except: # 아니면 실수형이므로
                self.symbol = Token.TokenSymbol.tReal
        elif type == Token.SymbolType.Operator: 
            self.symbol = self.getOperatorSymbol(token)
        elif type == Token.SymbolType.Literal:
            self.symbol = Token.TokenSymbol.tLiteral

sc = MiniScanner("test.txt")
while(sc.idx < len(sc.src)):
    tok = sc.getToken()
    print(tok)



