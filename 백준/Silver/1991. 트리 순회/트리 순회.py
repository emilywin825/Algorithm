def pre_order(root):
        if root!='.':
            print(root, end="")
            pre_order(tree[root][0])
            pre_order(tree[root][1])

def in_order(root):
        if root!='.':
            in_order(tree[root][0])
            print(root, end="")
            in_order(tree[root][1])

def post_order(root):
        if root!='.':
            post_order(tree[root][0])
            post_order(tree[root][1])
            print(root, end="")


n=int(input())
tree={}
for _ in range(n):
    root,left,right=input().split()
    tree[root]=[left,right]

pre_order('A')
print()
in_order('A')
print()
post_order('A')