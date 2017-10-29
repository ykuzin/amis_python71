print("\n Умова: N студентів отримали K яблук і розподілити їх між собою порівну. Неподілені яблука залишились у кошику. "
          "\n Скільки яблук отримає кожен студент? Скільки яблук залишиться в кошику?"
          "\n Програма отримує числа N і K. Вона повинна вивести два числа: відповіді на поставлені вище питання."
          "\n Вхідні дані: 2 цілих числа.  Кожне число користувач вводить в окремому рядку."
          "\n Вихідні дані: вивести два числа. Перше - кількість яблук у студента, друге - кількість яблук, що лишилось у кошику.\n")
N_studentiv = int(input(" Kilkist studentiv typu int: "))
K_yabluk = int(input(" Kilkist yabluk typu int: "))
print(" Kilkiist yabluk, cho otrymae student: ", K_yabluk // N_studentiv, "\n Kilkist yabluk, cho zalyshytsa v koshyku: ", K_yabluk % N_studentiv)
input()
