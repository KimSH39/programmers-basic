def solution(answers):
    answer = []
    
    first = [1, 2, 3, 4, 5] * 2000
    second = [2, 1, 2, 3, 2, 4, 2, 5]  * 2000
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]  * 2000
    
    scores = [0, 0, 0]
    
    for i in range(len(answers)):
        if answers[i] == first[i]:
            scores[0] += 1
            
    for i in range(len(answers)):
        if answers[i] == second[i]:
            scores[1] += 1
            
    for i in range(len(answers)):
        if answers[i] == third[i]:
            scores[2] += 1
            
    max_score = max(scores)
    
    for i, score in enumerate(scores):
        if score == max_score:
            answer.append(i + 1)
    
    return answer