clas1 = int(input('Number of students in the first group: '))
clas2 = int(input('Number of students in the second group: '))
clas3 = int(input('Number of students in the third group: '))
desk = clas1//2 + clas1%2 + clas2//2 + clas2%2 + clas3//2 + clas3%2
print('Number of desks', desk)