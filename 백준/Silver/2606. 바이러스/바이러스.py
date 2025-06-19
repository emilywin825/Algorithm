def dfs(computer):
    global num
    for i in network[computer]:
        if visited[i]==0:
            num+=1
            visited[i]=1
            dfs(i)
            
        
n=int(input()) #컴퓨터 수
m=int(input()) #네트워크 상에 직접 연결된 컴퓨터 쌍의 수

network=[[] for _ in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    network[a].append(b)
    network[b].append(a)
visited=[0]*(n+1)
visited[1]=1
num=0

dfs(1)
print(num)