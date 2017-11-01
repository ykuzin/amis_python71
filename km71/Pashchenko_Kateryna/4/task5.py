#Визначте, скільки з  трьох чисел дорівнюють один одному
a = int(input('Введіть ціле число:'))
b = int(input('Введіть ціле число:'))
c = int(input('Введіть ціле число:'))
if (a==b==c):
    ans=3
elif(a==b or c==b or a==c):
    ans=2
else:
    ans=0
print(ans)
