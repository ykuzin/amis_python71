print("Умова: Школа вирішила сформувати три нові групи учнів та надати їм окремі класи. "
          "\n У кожному класі необхідно встановити столи для учнів, у розрахунку, що за одним столом може сидіти не більше двох учнів. "
          "\n Яку мінімальну кількість столів необхідно придбати?"
          "\n Вхідні дані: 3 цілих числа - кількість учнів у кожній групі.  Кожне число користувач вводить в окремому рядку."
          "\n Вихідні дані: число - кількість столів\n")
group1 = int(input(" Kilkist uchniv u persiy gruppi typu int: "))
group2 = int(input(" Kilkist uchniv u druhiy gruppi typu int: "))
group3 = int(input(" Kilkist uchniv u tretiy gruppi typu int: "))
if group1%2 > 0:
    if group2%2 > 0:
        if group3%2 > 0:
            total = group1 // 2 + group2 // 2 + group3 // 2 + 3
        else:
            total = group1 // 2 + group2 // 2 + group3 // 2 + 2
    else:
        if group3%2 > 0:
            total = group1 // 2 + group2 // 2 + group3 // 2 + 2
        else:
            total = group1 // 2 + group2 // 2 + group3 // 2 + 1
else:
    if group2%2 > 0:
        if group3%2 > 0:
            total = group1 // 2 + group2 // 2 + group3 // 2 + 2
        else:
            total = group1 // 2 + group2 // 2 + group3 // 2 + 1
    else:
        if group3%2 > 0:
            total = group1 // 2 + group2 // 2 + group3 // 2 + 1
        else:
            total = group1 // 2 + group2 // 2 + group3 // 2
print(" Neobhidna kilkist part:", str(total), "shtuk")
input()
