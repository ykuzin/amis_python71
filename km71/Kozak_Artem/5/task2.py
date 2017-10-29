elements_count = int(input(" Enter count of elements: "))
elements = [input(" Enter "+str(element+1)+" element: ") for element in range(elements_count)]
elements.sort()
i = 1
pairs = 0
while i < elements_count:
    if elements[i] == elements[i-1]:
        pairs += 1
    i += 1
print(pairs)
