def solution(progresses, speeds):
    
    days = []
    
    # 남은 작업 일수 계산
    for i in range(len(progresses)):
        remaining = 100 - progresses[i]
        day = remaining // speeds[i]
        
        if remaining % speeds[i] != 0:
            day += 1
        days.append(day)
    
    answer = []
    
    while days:
        count = 1
        day = days.pop(0)
        while days and day >= days[0]:
            days.pop(0)
            count += 1
        answer.append(count)
        
    return answer