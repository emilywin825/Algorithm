T = int(input())
for test_case in range(1, T + 1):
    e,n=map(int,input().split())
    lis=list(map(int,input().split()))
    tree={}

    for i in range(0,len(lis),+2):
        if lis[i] in tree: 
            a=tree.get(lis[i])
            a.append(lis[i+1])
            tree[lis[i]]=a
        else:
            tree[lis[i]]=[lis[i+1]]
    
    def sub_tree(i):
        if i not in tree:
            return 1
        total=1
        for child in tree[i]:
            total+=sub_tree(child)
        return total
      
    res=sub_tree(n)
    print(f"#{test_case} {res}")