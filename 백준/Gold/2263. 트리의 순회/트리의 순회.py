import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

def preorder(in_left,in_right,post_left,post_right):
    if in_left > in_right:
        return

    #루트 노드
    root=postorder[post_right]
    print(root, end=" ") 

    #인오더에서 루트
    root_idx=inorder_mapping[root]
    offset=root_idx-in_left
    
    preorder(in_left,root_idx-1,post_left,post_left+offset-1)
    preorder(root_idx+1,in_right,post_left+offset,post_right-1)

n=int(input())
inorder=list(map(int,input().split()))
postorder=list(map(int,input().split()))

inorder_mapping={}

for i in range(len(inorder)):
    inorder_mapping[inorder[i]]=i

preorder(0,n-1,0,n-1)