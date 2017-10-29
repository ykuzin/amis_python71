x1_coord = int(input(" Enter coordinates of current location (x) from 1 to 8: "))
y1_coord = int(input(" Enter coordinates of current location (y) from 1 to 8: "))
x2_coord = int(input(" Enter coordinates of another location (x) from 1 to 8: "))
y2_coord = int(input(" Enter coordinates of another location (y) from 1 to 8: "))
if (x1_coord-y1_coord) % 2 == 1:
    colour1 = 1
else:
    colour1 = 0
if (x2_coord-y2_coord) % 2 == 1:
    colour2 = 1
else:
    colour2 = 0
input(" YES") if colour1 == colour2 else input(" NO")
