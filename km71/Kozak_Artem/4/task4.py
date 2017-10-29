year_nuber = int(input(" Enter nuber of the year: "))
if year_nuber%4==0 and year_nuber%100!=0:
    print(" LEAP")
elif year_nuber%400==0:
    print(" LEAP")
else:
    print(" COMMON")
input()
