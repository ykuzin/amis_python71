n = int(input('Number of pupils: '))
k = int(input('Number of apples: '))
apples_remain = k % n
got_apples = k // n
print('The apples are left: ', apples_remain, '\nGot a student: ', got_apples)