import math
a = [[0 for i in range(2)]for j in range(7)]
for i in range(7):                                                                                                      #розмістити 8 королев щоб вони не били одна одну мені не вдалося, тому я взяв 7 королев
    x, y = [int(i) - 1 for i in input('Enter the coordinates: ').split()]                                               #віднімаєм одиницю так як індексація розпочинається з 0
    a[i][0] = x
    a[i][1] = y
for i in range(7):                                                                                                      #фіксую кординату і порівню її з всіма іншими
    for j in range(7):
        if i != j:                                                                                                      #виключаю випадки коли кордината дорівнює сама собі
            if a[i][0] == a[j][0] or a[i][1] == a[j][1] or math.fabs(a[i][0] - a[j][0]) == math.fabs(a[i][1] - a[j][1]):#перевіряю чи є точки з однаковими х і у або різниця кординат однокова
                print('Queen beats Queen?\nYes')
                exit()
print('Queen beats Queen?\nNo')