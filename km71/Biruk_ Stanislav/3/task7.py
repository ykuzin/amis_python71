number = int(input('Enter the number: '))
age = number%1440      #Обнулимо добу якщо це буде потрібно
hour = age//60
minutes = age % 60
print('Hour: ', hour, '\n' 'Minutes: ', minutes)
