numbers = [int(i) for i in input('Enter numbers: ').split()]
for i in numbers:
    k = numbers.count(i)                                        #визначаю скільки раз елемент зустрічається в списку
    if k == 1:
        print(i, end=' ')