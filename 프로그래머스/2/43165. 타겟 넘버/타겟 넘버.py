def solution(numbers, target):
    
    def dfs(index, result):
        
        if index == len(numbers):
            if result == target:
                return 1
            else:
                return 0
        
        else:
            return dfs(index + 1, result + numbers[index]) + dfs(index + 1, result - numbers[index])
    
    return dfs(0, 0)