#Визначити, чи є вказаний рік високосним
year = int(input('Введіть рік:'))
if ((year%4==0) and (year%100!=0)):#рік високосний
    ans = "LEAP"
elif (year%400==0):#рік високосний
    ans = "LEAP"
else:
    ans = "СOMMON"
print(ans)

