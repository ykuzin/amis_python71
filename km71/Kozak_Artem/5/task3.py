elements_count = int(input(" Enter count of elements: "))
elements = [input(" Enter "+str(element+1)+" element: ") for element in range(elements_count)]
i = 0
answer = []
while i < elements_count:
    a = 0
    pairs = 0
    while a < elements_count:
        if elements[i] == elements[a]:
            pairs += 1
        a += 1
    if pairs == 1:
        answer.append(elements[i])
    i += 1
print(' '.join(answer))
