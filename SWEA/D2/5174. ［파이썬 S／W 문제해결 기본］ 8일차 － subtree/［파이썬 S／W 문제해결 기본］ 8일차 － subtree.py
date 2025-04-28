T = int(input())
for test_case in range(1, T + 1):
    e,n=map(int,input().split())
    lis=list(map(int,input().split()))
    tree={}
    res=1

    for i in range(0,len(lis),+2):
        if lis[i] in tree: 
            a=tree.get(lis[i])
            a.append(lis[i+1])
            tree[lis[i]]=a
        else:
            tree[lis[i]]=[lis[i+1]]
    
    def sub_tree(i):
        global res
        if i in tree:
            res+=len(tree[i])
            for k in tree.get(i):
                sub_tree(k)

                

    if n not in tree:
        res=1
    else:
        for i in tree.get(n):#루트 자식 가져오고
            res+=1
            if i in tree:
                sub_tree(i)

    print(f"#{test_case} {res}")