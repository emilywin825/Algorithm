#dfs로 풀어보겠음 -> 스택
def dfs(hap,start,now):
    global max
    
    if now==3:
        if max<hap and hap<=m:
            max=hap
        return
    
    
    for i in range(start,n):
        if hap+card[i]<=m and card[i] not in visit:
            visit.append(card[i])
            now_hap=hap+card[i]
            dfs(now_hap,start+1,now+1)
            visit.pop()


n,m=map(int,input().split())
card=list(map(int,input().split()))
max=-1
visit=[]
dfs(0,0,0)
print(max)