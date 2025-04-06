#dfs로 풀어보겠음 -> 스택
def dfs(hap,start,now):
    global maxx
    
    if now==3:
        if hap<=m:
            maxx=max(maxx,hap)
        return
    
    
    for i in range(start,n):
        if hap+card[i]<=m:
            dfs(hap+card[i],i+1,now+1)


n,m=map(int,input().split())
card=list(map(int,input().split()))
maxx=-1
visit=[]
dfs(0,0,0)
print(maxx)