#Дано три цілих числа. Вивести найменше з них.
a = int(input('Введіть ціле число:'))
b = int(input('Введіть ціле число:'))
c = int(input('Введіть ціле число:'))
if (a == b == c):
    ans = ('Числа рівні')
else:
    if(a<=b<=c):
        ans = a
    elif(b<=a<=c):
        ans = b
    elif(c<=b<=a):
        ans = c
    elif(c<=a<=b):
        ans = c
print(ans)




