def solution(n, wires):
    
    # 한 전력망의 송전탑 count
    def dfs(node):
        visited[node] = True
        return sum(dfs(i) for i in range(n)
                   if not visited[i] and graph[node][i]) + 1

    graph = [[False] * n for _ in range(n)]
    for a, b in wires:
        graph[a-1][b-1] = graph[b-1][a-1] = True

    answer = float('inf')
    
    # 선을 하나씩 끊는 과정
    for a, b in wires:
        # 끊음
        graph[a-1][b-1] = graph[b-1][a-1] = False
        visited = [False] * n
        # 두 전력망의 송전탑 개수 확인
        # 전체 전력망 송전탑 수 - dfs로 구한 한쪽 송전탑 수 * 2의 절댓값 = 그 차이가 두 전력망의 송전탑 개수 차이
        answer = min(answer, abs(n - 2 * dfs(0)))
        # 다시 연결
        graph[a-1][b-1] = graph[b-1][a-1] = True

    return answer
