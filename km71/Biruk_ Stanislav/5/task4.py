n, k = [int(i) for i in input('Enter the number of pins and the number of throws: ').split()]
a = [1 for i in range(n)]                                                                                               #заповнюємо список 1 (кеглі стоять)
for i in range(k):
    x, y = [int(i) for i in input('Enter a number pair: ').split()]                                                     #замінємо всі елементи як належать діапозону на 0 (кеглі впали)
    for i in range(x-1, y):                                                                                             #індексація розпочинається з нуля тому віднімаємо 1
        if a[i] == 1:
            a[i] = 0
for i in a:
    if i == 1:
        print('|', end='')
    else:
        print('.', end='')
