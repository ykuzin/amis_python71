list1 = []
list2 = []
kegls = int(input(' The number of kegls: '))
balls = int(input(' The number of balls: '))
for i in range(kegls+1):
	list1.append(i)
for _ in range(balls):
	balls_from = int(input(' From: '))
	balls_to = int(input(' To: '))
	for i in range(balls_from, balls_to+1):
		list2.append(i)
for i in list1:
	if i in list2:
		print('.', end = '')
	if i not in list2:
		print('|', end = '')
