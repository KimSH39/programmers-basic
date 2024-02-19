def solution(s):
    array = []
    
    # 일단 ( 나오면 저장
    # 만약 스택이 비었는데 )가 나오면 false
    # 무언가가 남아있으면 ( 일테니까 그거 하나뺌 
    
    for i in s:
        if i == '(':
            array.append(i)
        else:
            if array == []:
                return False
            array.pop()
        
    if len(array) == 0:
        return True
    else:
        return False