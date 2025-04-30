def r_p_s(a,b):
    if cards[a]==cards[b]:
        return a
    if cards[a]-cards[b]==1 or cards[a]-cards[b]==-2:
        return a
    return b

def game(start,end):
    if start==end:
        return start
    mid=(start+end)//2
    left=game(start,mid)
    right=game(mid+1,end)
    return r_p_s(left,right)

T = int(input())
for test_case in range(1, T + 1):
    n=int(input())
    cards=list(map(int,input().split()))
    winner = game(0, n - 1)
    print(f"#{test_case} {winner+1}")