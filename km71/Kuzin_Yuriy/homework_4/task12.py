n = int(input("Введітьзначення n "))
m = int(input("Введіть значення m  "))
k = int(input("Введіть значення k "))

if k < n*m and k%n == 0 or k%m == 0:
    print('YES')
else:
    print('NO')
