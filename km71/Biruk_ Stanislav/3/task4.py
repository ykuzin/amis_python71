n = int(input('Enter the number of students: '))
k = int(input('Enter the number of apples: '))
whole_part = k//n
remainder = k%n
print('Number of apples per student:', whole_part, '\n''Number of remaining apples', remainder)