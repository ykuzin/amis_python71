import math
x1_coord = int(input(" Enter coordinates of current location (x) from 1 to 8: "))
y1_coord = int(input(" Enter coordinates of current location (y) from 1 to 8: "))
x2_coord = int(input(" Enter coordinates of target location (x) from 1 to 8: "))
y2_coord = int(input(" Enter coordinates of target location (y) from 1 to 8: "))
if (math.fabs(x1_coord - x2_coord) == 1 and math.fabs(y1_coord - y2_coord) == 2) or (math.fabs(y1_coord - y2_coord) == 1 and math.fabs(x1_coord - x2_coord) == 2):
    input(" YES")
else:
    input(" NO")
