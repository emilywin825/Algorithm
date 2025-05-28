n=int(input())
card=list(map(int,input().split()))
m=int(input())
m_arr=list(map(int,input().split()))
card.sort()

card_count={}
for i in card:
    card_count[i] = card_count.get(i,0)+1

for j in m_arr:
    print(card_count.get(j,0), end=' ')