number = [input(" Enter "+str(element+1)+" number: ") for element in range(3)]
i = 1
if number[0] == number[1] or number[0] == number[2]:
    i += 1
if number[1] == number[2]:
    i += 1
print (0) if i == 1 else print(i)
input()

