def solution(myString, pat):
    
    trans = myString.replace("A", "x").replace("B", "A").replace("x", "B")
    
    if pat in trans:
        return 1
    else:
        return 0