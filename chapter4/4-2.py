#오오아래 / 오오위 / 왼왼아래 / 왼왼위
#오아래아래 / 왼아래아래 / 오위위 / 왼위위
input_data=input()
#a1
row = int(input_data[1]) #위아래
column = int(ord(input_data[0])) - int(ord('a'))+1 #행의 값을 아스키코드를 이용해 숫자로 변환
#좌우
steps = [(2,-1),(2,1),(-2,-1),(-2,1),(1,-2),(-1,-2),(1,2),(-1,2)]

result = 0

for step in steps :
    next_row = row + step[0]
    next_colum = column + step[1]

    if(next_row>=1 and next_row<=8 and next_colum>=1 and next_colum<=8) :
        result+=1

print(result)




