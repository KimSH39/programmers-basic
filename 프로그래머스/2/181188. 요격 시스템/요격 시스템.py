def solution(targets):
    
    targets.sort(key = lambda x:[x[1]])
    
    answer = 0
    e = 0
    
    for x in targets:
        if(x[0] >= e):
            e = x[1]
            answer += 1
    
    return answer