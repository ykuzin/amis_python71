x1 = int(input('Enter first number: '))
y1 = int(input('Enter second number: '))
x2 = int(input('Enter third number: '))
y2 = int(input('Enter third fourth: '))
if x1 == x2 or y1 == y2:
    answer = ('Yes')
elif x1 - x2 == y1 - y2:
    answer = ('Yes')
else:
    answer = ('No')
print('My answer is: ', answer)