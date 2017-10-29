n = int(input('Enter number: '))
hour = n % 1440 // 60
minutes = n %1440 % 60
print('Number of hours: ', hour, '\nNumber of minutes: ', minutes)