def dfs(L,P):
    global cnt
    if L==n:
        cnt+=1
        for j in range(P):
            print(chr(res[j]+64), end='')
        print()
    else:
        for i in range(1,27):
            if code[L]==i:
                res[P]=i
                dfs(L+1,P+1)
            elif i>=10 and code[L]==i//10 and code[L+1]==i%10:
                res[P]=i
                dfs(L+2,P+1)

if __name__=="__main__":
    code=list(map(int,input()))
    n=len(code) #종착점
    code.insert(n, -1) 
    res=[0]*(n+3)
    cnt=0
    dfs(0,0)
    print(cnt)