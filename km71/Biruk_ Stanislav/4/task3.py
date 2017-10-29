first_number = input('Enter first number: ')
second_number = input('Enter second number: ')
third_number = input('Enter third number: ')
min_number = first_number
if min_number > second_number:
    min_number = second_number
elif min_number > third_number:
    min_number = third_number
print('My answer is: ', min_number)