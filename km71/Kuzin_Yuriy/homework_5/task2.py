"""
Дано список чисел. Порахуйте, скільки в ньому пар елементів, рівних один одному. Вважається, що будь-які два елементи, рівні один одному утворюють одну пару, яку необхідно порахувати.
""" 
perv=  input("Введіть необхідний список ")
perv = perv.split()
perv = [int(x) for x in perv ] 
counter = {}
for i in perv:
   ss = i
   if (i not in counter): 
       counter[ss] = perv.count(i)
for i in counter :
    counter[i] = int(counter[i]* (counter[i]-1)/2)
print(counter)


