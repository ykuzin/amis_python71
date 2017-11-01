"""
Відомо, що на дошці 8 × 8 можна розставити 8 ферзів (королев) так, щоб вони не били один одного. Вам дана розстановка 8 ферзів на дошці, визначте, чи є серед них пара, що б'ють один одного.

Програма отримує на вхід вісім пар чисел, кожне число від 1 до 8 - координати 8 ферзів. Якщо ферзі не б'ють один одного, виведіть слово NO, інакше виведіть YES.

""" 
x= []
y =[]
for i in range(0,8):
    x1 = input("Введіть першу кординату ")
    y1 = input("Введіть другу координату ")
    x.append(x1)
    y.append(y1)
x=[int(k) for k in x]
y=[int(d) for d in y]
control = "NO"
for i in range(8):
    for j in range(8):
        if x[i] == x[j]:
            control = "YES" 

for i in range(8):
    for j in range(8):
        if y[i] == y[j]:
            control = "YES" 

for i in range(8):
    for j in range(8):
        if abs(x[i] - x[j]) == abs(y[i] - y[j]):
            control = "YES"
print(control)
    
