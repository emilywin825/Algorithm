def DFS(num):
    if num==0:
        return
    else:
        DFS(num//2)
        print(num%2,end='')

if __name__=="__main__":
    n=int(input())
    DFS(n)