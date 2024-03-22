def solution(new_id):
    answer = ''
    new_id = level1(new_id)
    new_id = level2(new_id)
    new_id = level3(new_id)
    new_id = level4(new_id)
    new_id = level5(new_id)
    new_id = level6(new_id)
    answer = level7(new_id)
    
    return answer

def level1(new_id):
    return new_id.lower()

def level2(new_id):
    id = ""
    for i in range(len(new_id)):
        if new_id[i].isdigit() or new_id[i].isalpha() or new_id[i] == '-' or new_id[i] == '_' or new_id[i] == '.':
            id += new_id[i]
    return id

def level3(new_id):
    check = False
    id = ""
    for s in new_id:
        if s == '.':
            if not check:
                check = True
                id += s
            continue
        else:
            if check:
                check = False
            id += s
    return id

def level4(new_id):
    if new_id == "":
        return new_id
    id = list(new_id)
    if id[0] == '.':
        id.pop(0)
    elif id[-1] == ".":
        id.pop()
    return "".join(id)

def level5(new_id):
    if new_id == "":
        new_id = "a"
    return new_id

def level6(new_id):
    id = list(new_id)
    if len(id) > 15:
        id = id[:15]
    if id[-1] == ".":
        id.pop()
    return "".join(id)
        
def level7(new_id):
    if len(new_id) == 1:
        new_id += new_id[-1] + new_id[-1]
    elif len(new_id) == 2:
        new_id += new_id[-1]
    return new_id
            
        
            