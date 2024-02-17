def solution(numbers):
    
    # 숫자를 문자로 변경
    numbers = [str(x) for x in numbers]
    
    numbers.sort(key = lambda x: (x * 4)[:4], reverse = True)
    
    if numbers[0] == '0':
        answer = '0'
    else:
        answer = ''.join(numbers) 
    
    return answer