"""
Дано список. Виведіть ті його елементи, які зустрічаються в списку тільки один раз. Елементи потрібно виводити в тому порядку, в якому вони зустрічаються в списку.
"""
spisok = input("Введіть необхідний список")
spisok = spisok.split()
spisok =[int(s) for s in spisok]
counter = {}
for i in spisok:
   ss = i
   if (i not in counter): 
       counter[ss] = spisok.count(i)
       if counter[ss] ==1 :
           print(ss)

