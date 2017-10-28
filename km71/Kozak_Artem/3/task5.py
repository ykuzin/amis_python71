print("\n Умова: Напишіть програму, яка зчитує ціле число і друкує його попереднє і наступне значення за форматом:"
          "\n The next number for the number 179 is 180."
          "\n The previous number for the number 179 is 178."
          "\n Вхідні дані: ціле число"
          "\n Вихідні дані: два рядки за наведеним у завдання форматом.\n")
number = int(input(" Cile chislo: "))
print(" The next number for the number", number, "is", str(number + 1)+".", "\n The previous number for the number ", number, " is ", str(number - 1)+".")
input()
