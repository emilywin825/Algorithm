def solution(numbers, target):
    answer=0
    arr=[]
    
    def dfs(idx):
        nonlocal answer
        if len(arr)==len(numbers) and sum(arr)==target:
            answer+=1
            return
        if idx>=len(numbers):
            return
        
        arr.append(numbers[idx])
        dfs(idx+1)
        arr.pop()
        arr.append(-numbers[idx])
        dfs(idx+1)
        arr.pop()
        
    dfs(0)
    return answer