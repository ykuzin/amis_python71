numbers = [int(i) for i in input('Enter numbers: ').split()]
k = 0
for i in numbers:
    for j in numbers:
        if i == j:
            k +=1    #Кожне число послідовності дорівнює саме собі, тому віднімемо кількість символів
print('The number of identical pairs is equal: ', k - len(numbers))