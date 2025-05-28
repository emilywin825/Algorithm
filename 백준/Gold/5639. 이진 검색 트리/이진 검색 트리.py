# import sys
# input=sys.stdin.readline
# sys.setrecursionlimit(10**6)

# def postorder(start,end):
#     if start>end:
#         return
#     root=preorder[start]
#     idx=start+1

#     while idx<=end and preorder[idx]<root:
#         idx+=1
    
#     postorder(start+1,idx-1)
#     postorder(idx,end)
#     print(root)

# preorder=[]
# while True:
#     try:
#         preorder.append(int(input()))
#     except:
#         break

# postorder(0,len(preorder)-1)


import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

def postorder(arr):
    if len(arr)==0:
        return
    
    left,right=[],[]
    root=arr[0]
    for i in range(1,len(arr)):
        if root<arr[i]:
            left=arr[1:i]
            right=arr[i:]
            break
    else:
        left=arr[1:]
    postorder(left)
    postorder(right)
    print(root)

preorder=[]
while True:
    try:
        preorder.append(int(input()))
    except:
        break

postorder(preorder)