first_number = input('Enter first number: ')
second_number = input('Enter second number: ')
third_number = input('Enter third number: ')
if first_number == second_number == third_number:
    answer = ('3')
elif first_number == second_number != third_number or first_number != second_number == third_number:
    answer = ('2')
else:
    answer = ('0')
print('My answer is:', answer)