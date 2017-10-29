growthStudent = [int(i) for i in input('Enter growth of people: ').split()]
growthPetya = int(input('Enter growth of Petya: '))
sequenceNumber = 1
for i in growthStudent:
    if i >= growthPetya:
        sequenceNumber +=1
print('sequence number of Petya:',sequenceNumber)