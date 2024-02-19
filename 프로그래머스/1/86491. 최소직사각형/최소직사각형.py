def solution(sizes):
    answer = 0
    
    dum = [0, 0]
    
    min1 = []
    min2 = []
    
    for size in sizes:
        if size[0] > size[1]:
            dum[0] = size[1] # dum[0] = 50 size[1] = 50
            size[1] = size[0]  # size[1] = 60
            size[0] = dum[0] # size[0] = 50
            
        min1.append(size[0])
        min2.append(size[1])
            
    answer = max(min1) * max(min2)
    
    return answer