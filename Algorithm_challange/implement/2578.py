bingo = []
moderator = []

def checkColumn(): # 열 체크
    number=0
    for i in range(5): 
        x=0
        for j in range(5):
            if(bingo[j][i]==0):
                x+=1
        if(x==5):
            number+=1
    return number


def checkRow(): # 행 체크
    number=0
    for i in range(5):
        x=0
        for j in range(5):
            if(bingo[i][j]==0):
                x+=1
        if(x==5):
            number+=1
    return number



def checkDiagonal(): #대각선 체크 [0][0] [1][1]
    number=0
    x=0
    for i in range(5):
        if(bingo[i][i]==0):
            x+=1
    if x == 5:
        number+=1
        
    x=0
    for i in range(5):
        if(bingo[i][4-i]==0):
            x+=1
    if x==5:
        number+=1

    return number

for _ in range(5):
    bingo.append(list(map(int, input().split())))

for _ in range(5):
    data = input().split()
    for i in data:
        moderator.append(int(i))

for i in range(25):
    num = moderator[i]
    for j in range(5):
        for k in range(5):
            if bingo[j][k] == num:
                bingo[j][k]=0
    number = checkColumn() + checkDiagonal() + checkRow()
    
    if number>=3:
        print(i+1)
        break