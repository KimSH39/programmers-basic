def solution(board, moves):
    answer = 0
    a = [] # 바구니
    
    for move in moves:
        for i in range(len(board)):
            # board[i]는 층수, move는 가로 위치
            if board[i][move-1] != 0:
                # 인형 뽑아서 바구니 넣고
                a.append(board[i][move-1])
                # 그 위치 비우기
                board[i][move-1] = 0
                
                if len(a) >= 2:
                    if a[-1] == a[-2]:
                        a.pop()
                        a.pop()
                        
                        answer += 2
                        
                break
    
    return answer