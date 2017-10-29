import math
x = float(input(' Enter number X: '))
if x == 0:
    print(' Sign x = 0')
else:
    print(' Sign x =', round(x/math.fabs(x)))
input()
