def solution(arr):
    
    answer = []
    
    for i in range(len(arr)):
        answer.append(arr[i])
        
        if i > 0 and arr[i] == arr[i-1]:
            answer.pop()

    return answer