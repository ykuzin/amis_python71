"""
Умова: Вивести результат функціїsign(x), що визначається наступним чином: 
sign(x) = 1, if x > 0, 
sign(x) = -1, if x < 0, 
sign(x) = 0, if x = 0..

Вхідні дані: користувач вводить дійсне число.

Вихідні дані: вивести результат sign.
"""
def sign(x): 

    if x>0:
        return 1
    elif x<0:
        return -1
    else:
        return 0

z = float(input("Введіть число "))
print(sign(z))
