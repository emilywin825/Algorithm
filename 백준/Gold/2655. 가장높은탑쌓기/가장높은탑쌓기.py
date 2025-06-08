n=int(input())
#넓이,높이,무게
tower=[]
track=[-1 for _ in range(n)]

for i in range(n):
    m,h,w=map(int,input().split())
    tower.append((m,h,w,i+1))
tower.sort(key=lambda x:x[2])
dp=[tower[i][1] for i in range(n)]


for i in range(n):
    for j in range(i):
        if tower[i][0]>tower[j][0] and tower[i][2]>tower[j][2]:
            if dp[i]<tower[i][1]+dp[j]:
                dp[i]=tower[i][1]+dp[j]
                track[i]=j

    
maxx_target=dp.index(max(dp)) 
res=[] 
while maxx_target!=-1:
    res.append(tower[maxx_target][3])
    maxx_target=track[maxx_target]

print(len(res))
for i in reversed(res):
    print(i)