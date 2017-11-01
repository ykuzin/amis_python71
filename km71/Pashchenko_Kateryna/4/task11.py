#Визначити, чи може кінь перейти з першої клітини у другу за один хід
x1 = int(input('Введіть номер рядка першої клітинки:'))
y1 = int(input('Введіть номер стовпчика пешої клiтинки:'))
x2 = int(input('Введіть номер рядка  другої клітинки:'))
y2 = int(input('Введіть номер стовчика другої клiтинки:'))
if ((1<=y2<=8) and (1<=x1<=8) and (1<=x2<=8) and (1<=y1<=8)):
    if ((x1==x2) or (y1==y2)):
        answer = 'NO'
    else:
        if ((x2 == x1+2) and (y2 == y1 -1)):
            answer = 'YES'
        elif((y2 == y1-1) and (x2 == x1+2)):
            answer = 'YES'
        elif((x2==x1 - 2)and (y2 == y1 +1)):
            answer = 'YES'
        elif((x2 == x1 +1)and(y2 == y1 + 2)):
            answer = 'YES'
        elif((x2 == x1 -1) and (y2 == y1 +2)):
            answer = 'YES'
        elif((x2 == x1 +2) and (y2 == y1 +1)):
            answer = 'YES'
        elif((x2 == x1 -1) and (y2 == y1 -2)):
            answer = 'YES'
        elif((x2 == x1 -2) and (y2 == y1 -1)):
            answer = 'YES'
        else:
            answer = 'NO'
print(answer)

